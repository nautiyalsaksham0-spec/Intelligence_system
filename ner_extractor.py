from transformers import pipeline
import transformers
transformers.logging.set_verbosity_error()
def initialize_ner():
    print("Loading AI Named Entity Recognition Model (This might take a minute the first time)...")
    ner_model=pipeline("ner",model="dslim/bert-base-NER",aggregation_strategy="simple")
    return ner_model

def extract_entities(analyzed_events_list,ner_model):
    print("Initiating AI Entity Extraction Pipeline...")
    final_intelligence = []
    for event in analyzed_events_list:
        text_to_scan=event['original_details'] 
        raw_entities=ner_model(text_to_scan)
        locations=[]
        organizations=[]
        people=[]
        for entity in raw_entities:
            word=entity['word']
            tag=entity['entity_group']
            if tag=='LOC'and word not in locations:
                locations.append(word)
            elif tag=='ORG' and word not in organizations:
                organizations.append(word)
            elif tag=='PER' and word not in people:
                people.append(word)
        final_intelligence.append({
            "report_title":event['report_title'],
            "ai_summary":event.get('ai_summary',"No summary provided"),
            "original_details": event['original_details'],
            "locations_spotted":locations,
            "organizations_involved":organizations,
            "key_people":people
        })
    print(f"Success:Extracted entities from {len(final_intelligence)}events!\n")
    return final_intelligence
if __name__=="__main__":
    test_data=[
        {
            "report_title":"Diplomatic Summit Alert",
            "original_details":"The United Nations held a closed-door security summit in Geneva today. Secretary General Antonio Guterres discussed the ongoing border situation with senior representatives from the European Union.",
            "ai_summary":"United Nations holds security summit in Geneva with European Union."
        }
    ]
    ai_ner=initialize_ner()
    results=extract_entities(test_data,ai_ner)
    print("EXTRACTED INTELLIGENCE")
    print(f"Report:{results[0]['report_title']}")
    print(f"Where:{results[0]['locations_spotted']}")
    print(f"Who (Groups):{results[0]['organizations_involved']}")
    print(f"Who (People):{results[0]['key_people']}")