import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta

# Base URL pattern
BASE_URL = "https://reports-public.ieso.ca/public/IntertieScheduleFlow/PUB_IntertieScheduleFlow_{date}.xml"

# Generate date range
def generate_dates(start="2025-05-24", end="2025-06-21"):
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")
    while start_date <= end_date:
        yield start_date.strftime("%Y%m%d")
        start_date += timedelta(days=1)

# Extract data from a single XML
def extract_data_from_xml(xml_content, report_date):
    soup = BeautifulSoup(xml_content, 'xml')
    zones = soup.find_all('IntertieZone')
    records = []

    for zone in zones:
        zone_name = zone.find('IntertieZoneName').text

        actuals = zone.find_all('Actual')
        for actual in actuals:
            hour = actual.find('Hour').text
            interval = actual.find('Interval').text
            flow = actual.find('Flow').text
            records.append({
                'Date': report_date,
                'Zone': zone_name,
                'Hour': int(hour),
                'Interval': int(interval),
                'Flow': float(flow)
            })
    return records

# Main scraping logic
def main():
    all_data = []

    for date_str in generate_dates():
        url = BASE_URL.format(date=date_str)
        print(f"Fetching: {url}")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            day_data = extract_data_from_xml(response.content, date_str)
            all_data.extend(day_data)
        except requests.RequestException as e:
            print(f"Failed to fetch data for {date_str}: {e}")

    # Convert to DataFrame and save to Excel
    if all_data:
        df = pd.DataFrame(all_data)
        df.sort_values(by=['Date', 'Zone', 'Hour', 'Interval'], inplace=True)
        df.to_excel('data_intertie.xlsx', index=False)
        print("Data successfully written to data_intertie.xlsx")
    else:
        print("No data was retrieved.")

if __name__ == "__main__":
    main()
