import requests
import xml.etree.ElementTree as ET
import pandas as pd
from datetime import datetime, timedelta
import os

BASE_URL = "https://reports-public.ieso.ca/public/VGForecastSummary/PUB_VGForecastSummary_{date}.xml"
NAMESPACE = {"ieso": "http://www.ieso.ca/schema"}  # Define namespace prefix

def generate_date_range(start_str="2025-06-02", end_str="2025-06-21"):
    start = datetime.strptime(start_str, "%Y-%m-%d")
    end = datetime.strptime(end_str, "%Y-%m-%d")
    while start <= end:
        yield start.strftime("%Y%m%d")
        start += timedelta(days=1)

def parse_forecast_summary(xml_text: str, date: str) -> pd.DataFrame:
    root = ET.fromstring(xml_text)
    data = []
    for fuel in root.findall(".//ieso:FuelData", NAMESPACE):
        fuel_type = fuel.find("ieso:FuelType", NAMESPACE).text
        for resource in fuel.findall(".//ieso:ResourceData", NAMESPACE):
            zone_name = resource.find("ieso:ZoneName", NAMESPACE).text
            for forecast in resource.findall("ieso:EnergyForecast", NAMESPACE):
                forecast_date = forecast.find("ieso:ForecastDate", NAMESPACE).text
                for interval in forecast.findall("ieso:ForecastInterval", NAMESPACE):
                    hour = interval.find("ieso:ForecastHour", NAMESPACE).text
                    output = interval.find("ieso:MWOutput", NAMESPACE).text
                    data.append({
                        "FileDate": date,
                        "FuelType": fuel_type,
                        "Zone": zone_name,
                        "ForecastDate": forecast_date,
                        "Hour": int(hour),
                        "MWOutput": float(output)
                    })
    return pd.DataFrame(data)

all_data = []
missing_files = []

for date in generate_date_range("2025-06-02", "2025-06-21"):
    url = BASE_URL.format(date=date)
    try:
        print(f"Trying: {url}")
        response = requests.get(url)
        if response.ok:
            df = parse_forecast_summary(response.text, date)
            if not df.empty:
                all_data.append(df)
        else:
            print(f"❌ Failed to fetch valid file for {date}")
            missing_files.append(date)
    except Exception as e:
        print(f"❌ Error on {date}: {e}")
        missing_files.append(date)

# Export data
if all_data:
    full_df = pd.concat(all_data)
    full_df.to_excel("data_vg_forecast.xlsx", index=False)
    print("✅ Data successfully written to data_sbg_forecast.xlsx")
else:
    print("⚠️ No data retrieved in the specified date range.")

# Log missing files
if missing_files:
    with open("missing_vg_files.txt", "w") as f:
        for date in missing_files:
            f.write(date + "\n")
    print("📄 Missing dates logged to missing_vg_files.txt")
