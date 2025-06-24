import requests
import xml.etree.ElementTree as ET
import pandas as pd
from datetime import datetime, timedelta

# URL template
BASE_URL = "https://reports-public.ieso.ca/public/Adequacy3/PUB_Adequacy3_{date}.xml"

# Date range generator (fixed to your request)
def generate_date_range(start_str="2025-06-01", end_str="2025-07-21"):
    start = datetime.strptime(start_str, "%Y-%m-%d")
    end = datetime.strptime(end_str, "%Y-%m-%d")
    current = start
    while current <= end:
        yield current.strftime("%Y%m%d")
        current += timedelta(days=1)

def is_valid_xml(text: str) -> bool:
    return text.lstrip().startswith('<?xml')

def parse_adequacy_xml(xml_text: str) -> pd.DataFrame:
    ns = {'ns': 'http://www.ieso.ca/schema'}
    root = ET.fromstring(xml_text)
    delivery_date = root.find('.//ns:DeliveryDate', ns).text

    supplies = [
        {
            'DeliveryHour': int(s.find('ns:DeliveryHour', ns).text),
            'TotalSupply_MW': int(s.find('ns:EnergyMW', ns).text)
        }
        for s in root.findall('.//ns:TotalSupplies/ns:Supply', ns)
    ]

    demands = [
        {
            'DeliveryHour': int(d.find('ns:DeliveryHour', ns).text),
            'OntarioDemand_MW': int(d.find('ns:EnergyMW', ns).text)
        }
        for d in root.findall('.//ns:ForecastOntDemand/ns:Demand', ns)
    ]

    df = pd.merge(pd.DataFrame(supplies), pd.DataFrame(demands), on='DeliveryHour')
    df['DeliveryDate'] = delivery_date
    return df[['DeliveryDate', 'DeliveryHour', 'TotalSupply_MW', 'OntarioDemand_MW']]

def main():
    all_data = []
    for date_str in generate_date_range():
        url = BASE_URL.format(date=date_str)
        print(f"→ Fetching {url}")
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code != 200:
                print(f"  [SKIP] HTTP {resp.status_code}")
                continue
            if not is_valid_xml(resp.text):
                print(f"  [SKIP] Not valid XML for {date_str}")
                continue
            try:
                df = parse_adequacy_xml(resp.text)
                all_data.append(df)
                print(f"  [OK] Parsed {len(df)} hourly records for {date_str}")
            except ET.ParseError as e:
                print(f"  [FAIL] XML ParseError on {date_str}: {e}")
        except requests.RequestException as e:
            print(f"  [ERROR] Request failed for {date_str}: {e}")

    if not all_data:
        print("No valid data collected.")
        return

    final_df = pd.concat(all_data, ignore_index=True)
    final_df.sort_values(['DeliveryDate', 'DeliveryHour'], inplace=True)
    final_df.to_excel("scraped_data.xlsx", index=False)
    print(f"\n✅ SUCCESS: Exported {len(final_df)} rows to scraped_data.xlsx")

if __name__ == "__main__":
    main()
