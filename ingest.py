import requests
import xml.etree.ElementTree as ET
def fetch_live_events():
    print("Initiating Data Ingestion Pipeline...")
    url="http://feeds.bbci.co.uk/news/world/rss.xml"
    response=requests.get(url,timeout=10)
    if response.status_code==200:
        print("Success: Connected to live feed!\n")
        root=ET.fromstring(response.content)
        events=[]
        for item in root.findall('.//item')[:5]:
            title=item.find('title').text
            description=item.find('description').text
            events.append({
                "report_title": title, 
                "original_details": description
            })
        return events
    else:
        print(f"CRITICAL: Failed to fetch data. Status code: {response.status_code}")
        return []
if __name__=="__main__":
    raw_intelligence_data=fetch_live_events()
    for i,event in enumerate(raw_intelligence_data,1):
        print(f"--- INCOMING EVENT {i} ---")
        print(f"REPORT : {event['report_title']}")
        print(f"DETAILS : {event['original_details']}\n")