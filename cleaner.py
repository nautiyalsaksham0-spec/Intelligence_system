import re
def clean_text(raw_text):
    if not raw_text:
        return ""
    text=re.sub(r'<.*?>', ' ',raw_text)
    text=text.replace("&amp;","&").replace("&quot;",'"').replace("&apos;","'")
    text=re.sub(r'\s+',' ',text)
    return text.strip()
def preprocess_events(events_list):
    print("Initiating Data Cleaning Pipeline...")
    cleaned_events=[]
    for event in events_list:
        clean_title=clean_text(event['report_title'])
        clean_details=clean_text(event['details'])
        cleaned_events.append({
            "report_title":clean_title,
            "details":clean_details
        })
    print(f"Success: Scrubbed{len(cleaned_events)}events clean!\n")
    return cleaned_events
if __name__=="__main__":
    messy_simulated_data=[
        {
            "report_title":"Breaking:Military Movement &amp; Alert!",
            "details":"<p>Heavy troop buildup spotted.</p> <br> Wait, false alarm.   \n\n  Stand down."
        }
    ]
    print("BEFORE CLEANING")
    print(messy_simulated_data[0])
    print("\n")
    clean_data=preprocess_events(messy_simulated_data)
    print("AFTER CLEANING")
    print(clean_data[0])