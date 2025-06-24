import requests
import xml.etree.ElementTree as ET
import pandas as pd
from datetime import datetime, timedelta

# URL pattern for VG Forecast Summary files
BASE_URL = "https://reports-public.ieso.ca/public/VGForecastSummary/PUB_VGForecastSummary_{date}.xml"

# Generate date range
def generate_date_range(start="2025-05-23", end="2025-06-22"):
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")
    while start_date <= end_date:
        yield start_date.strftime("%Y%m%d")
        start_date += timedelta(days=1)

# Parse a single VG forecast XML document
def parse_vg_forecast(xml_text: str, fetch_date: str) -> pd.DataFrame:
    ns = {'ns': 'http://www.ieso.ca/schema'}
    root = ET.fromstring(xml_text)
    records = []

    for fuel_data in root.findall(".//ns:FuelData", ns):
        fuel_type = fuel_data.findtext("ns:FuelType", default="", namespaces=ns)

        for resource in fuel_data.findall(".//ns:ResourceData", ns):
            zone = resource.findtext("ns:ZoneName", default="", namespaces=ns)

            for forecast in resource.findall(".//ns:EnergyForecast", ns):
                forecast_date = forecast.findtext("ns:ForecastDate", default="", namespaces=ns)

                for interval in forecast.findall(".//ns:ForecastInterval", ns):
                    hour = interval.findtext("ns:ForecastHour", default="", namespaces=ns)
                    mw_output = interval.findtext("ns:MWOutput", default="", namespaces=ns)

                    records.append({
                        "FetchDate": fetch_date,
                        "ForecastDate": forecast_date,
                        "ForecastHour": hour,
                        "ZoneName": zone,
                        "FuelType": fuel_type,
                        "MWOutput": mw_output
                    })

    return pd.DataFrame(records)

# Main execution function
def main():
    all_data = pd.DataFrame()

    for date_str in generate_date_range():
        url = BASE_URL.format(date=date_str)
        print(f"Fetching: {url}")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            df = parse_vg_forecast(response.text, fetch_date=date_str)
            if df.empty:
                print(f"⚠️ No data for {date_str}")
            all_data = pd.concat([all_data, df], ignore_index=True)
        except requests.RequestException as e:
            print(f"❌ Failed to fetch {date_str}: {e}")

    if not all_data.empty:
        all_data.sort_values(by=["ForecastDate", "ForecastHour", "ZoneName", "FuelType"], inplace=True)
        all_data.to_excel("data_forecast_variable.xlsx", index=False)
        print("✅ Data saved to data_vg_forecast.xlsx")
    else:
        print("⚠️ No data retrieved in the entire date range.")

if __name__ == "__main__":
    main()
