import time
import summarizer
import ner_extractor
import classifier

def run_intelligence_pipeline():
    print("\n"+"="*60)
    print(" INITIATING AI-TIES TACTICAL INTELLIGENCE PIPELINE")
    print("="*60+"\n")
    clean_events_list=[
        {
            "report_title":"Border Region Escalation",
            "original_details":"Intelligence analysts have detected a massive influx of armored vehicles and infantry units moving toward the northern border region near Geneva over the last 48 hours. Satellite imagery confirms the establishment of temporary forward operating bases. The United Nations and European Union are monitoring the situation closely while Secretary General Antonio Guterres prepares a statement."
        },
        {
            "report_title": "City Hall Meeting",
            "original_details": "Local politicians met to discuss the new budget for road repairs. The meeting concluded peacefully at 4 PM with no incidents or protests."
        }
    ]
    print("[SYSTEM] Allocating memory and booting AI Engines...")
    ai_summarizer=summarizer.initialize_summarizer()
    ai_ner=ner_extractor.initialize_ner()
    ml_classifier=classifier.train_threat_classifier()
    print("[SYSTEM] All AI Models successfully loaded into RAM.\n")
    print("[PIPELINE] Stage 1: Compressing raw reports into tactical summaries...")
    summarized_data=summarizer.summarize_events(clean_events_list, ai_summarizer)
    print("[PIPELINE] Stage 2: Extracting target entities (WHO and WHERE)...")
    ner_data=ner_extractor.extract_entities(summarized_data, ai_ner)
    print("[PIPELINE] Stage 3: Calculating Threat Matrix...")
    final_intelligence=classifier.classify_events(ner_data,ml_classifier)
    print("\n"+"="*60)
    print("  FINAL TACTICAL BRIEFING")
    print("="*60)
    
    for intel in final_intelligence:
        print(f"\n[ALERT THREAD] {intel['report_title']}")
        print(f"THREAT LEVEL:  [{intel['threat_level']}]")
        print(f"AI SUMMARY:    {intel['ai_summary']}")
        print(f"LOCATIONS:     {intel.get('locations_spotted', [])}")
        print(f"ORGANIZATIONS: {intel.get('organizations_involved', [])}")
        print(f"KEY PEOPLE:    {intel.get('key_people', [])}")
        print("-"*60)
        
    print("\n[SYSTEM] Pipeline execution complete. Shutting down securely.")

if __name__=="__main__":
    run_intelligence_pipeline()