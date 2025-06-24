import requests
import xml.etree.ElementTree as ET
import pandas as pd
from datetime import datetime, timedelta

BASE_URL = "https://reports-public.ieso.ca/public/GenOutputCapability/PUB_GenOutputCapability_{date}.xml"

# Generate a list of dates between the range
def generate_date_range(start_str="2025-05-23", end_str="2025-06-22"):
    start = datetime.strptime(start_str, "%Y-%m-%d")
    end = datetime.strptime(end_str, "%Y-%m-%d")
    while start <= end:
        yield start.strftime("%Y%m%d")
        start += timedelta(days=1)

def parse_gen_output_format(xml_text: str, date: str) -> pd.DataFrame:
    root = ET.fromstring(xml_text)
    data = []

    for generator in root.findall(".//Generator"):
        unit_name = generator.findtext("UnitName", "").strip()
        unit_type = generator.findtext("UnitType", "").strip()

        # Get Capability and Output as parallel lists of 24 values
        capability = generator.find("Capability")
        output = generator.find("Output")

        if capability is None or output is None:
            continue

        cap_values = [float(c.text) if c is not None else None for c in capability.findall("Hour")]
        out_values = [float(o.text) if o is not None else None for o in output.findall("Hour")]

        for hour in range(1, 25):  # Hours 1 to 24
            data.append({
                "Date": date,
                "Hour": hour,
                "UnitName": unit_name,
                "UnitType": unit_type,
                "Capability": cap_values[hour - 1] if hour - 1 < len(cap_values) else None,
                "Output": out_values[hour - 1] if hour - 1 < len(out_values) else None
            })

    return pd.DataFrame(data)

def main():
    all_data = []
    for date_str in generate_date_range():
        url = BASE_URL.format(date=date_str)
        print(f"📡 Fetching: {url}")
        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200 or not response.text.strip().startswith("<?xml"):
                print(f"  ⛔ Skipped: HTTP {response.status_code}")
                continue

            df = parse_gen_output_format(response.text, date_str)
            if not df.empty:
                all_data.append(df)
                print(f"  ✅ Parsed {len(df)} rows.")
            else:
                print(f"  ⚠️ No data in file.")
        except Exception as e:
            print(f"  ❌ Failed to process {date_str}: {e}")

    if all_data:
        final_df = pd.concat(all_data, ignore_index=True)
        final_df.sort_values(by=["Date", "UnitName", "Hour"], inplace=True)
        final_df.to_excel("gop.xlsx", index=False)
        print("\n🎉 DONE: Exported all generator capability/output data to gop.xlsx")
    else:
        print("\n❌ No data was collected.")

# Run it
if __name__ == "__main__":
    main()
