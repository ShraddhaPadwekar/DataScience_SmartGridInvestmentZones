import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta

# URL pattern
BASE_URL = "https://reports-public.ieso.ca/public/GenOutputCapability/PUB_GenOutputCapability_{date}.xml"

# Generate date range
def generate_dates(start="2025-05-23", end="2025-06-22"):
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")
    while start_date <= end_date:
        yield start_date.strftime("%Y%m%d")
        start_date += timedelta(days=1)

# Parse a single XML content
def extract_data_from_xml(xml_content, report_date):
    soup = BeautifulSoup(xml_content, "xml")
    data = []

    for gen in soup.find_all("Generator"):
        name_tag = gen.find("GeneratorName")
        if name_tag is None:
            continue
        name = name_tag.text.strip()

        # Parse output values safely
        outputs = {}
        for out in gen.find_all("Output"):
            hour_tag = out.find("Hour")
            mw_tag = out.find("EnergyMW")
            if hour_tag and mw_tag:
                try:
                    hour = int(hour_tag.text)
                    mw = float(mw_tag.text)
                    outputs[hour] = mw
                except ValueError:
                    continue

        # Parse capability values safely
        capabilities = {}
        for cap in gen.find_all("Capability"):
            hour_tag = cap.find("Hour")
            mw_tag = cap.find("EnergyMW")
            if hour_tag and mw_tag:
                try:
                    hour = int(hour_tag.text)
                    mw = float(mw_tag.text)
                    capabilities[hour] = mw
                except ValueError:
                    continue

        for hour in range(1, 24):  # Only hours 1 to 23 are expected
            data.append({
                "Date": report_date,
                "Hour": hour,
                "GeneratorName": name,
                "Output(MW)": outputs.get(hour),
                "Capability(MW)": capabilities.get(hour)
            })

    return data

# Main function
def main():
    all_data = []

    for date_str in generate_dates():
        url = BASE_URL.format(date=date_str)
        print(f"Fetching: {url}")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            day_data = extract_data_from_xml(response.content, date_str)
            if not day_data:
                print(f"⚠️ No generator records found in {date_str}")
            all_data.extend(day_data)
        except requests.RequestException as e:
            print(f"❌ Failed for {date_str}: {e}")

    if all_data:
        df = pd.DataFrame(all_data)
        df.sort_values(by=["Date", "GeneratorName", "Hour"], inplace=True)
        df.to_excel("data_gen_output.xlsx", index=False)
        print("✅ Data saved to data_gen_output.xlsx")
    else:
        print("⚠️ No data retrieved for the specified date range.")

if __name__ == "__main__":
    main()
