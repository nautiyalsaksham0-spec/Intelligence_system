import time
import summarizer
import ner_extractor

def run_intelligence_pipeline():
    print("\n"+"="*60)
    print(" INITIATING AI-TIES TACTICAL INTELLIGENCE PIPELINE")
    print("="*60+"\n")
    clean_events_list=[
        {
            "report_title":"Border Region Escalation",
            "details":"Intelligence analysts have detected a massive influx of armored vehicles and infantry units moving toward the northern border region near Geneva over the last 48 hours. Satellite imagery confirms the establishment of temporary forward operating bases. The United Nations and European Union are monitoring the situation closely while Secretary General Antonio Guterres prepares a statement."
        }
    ]
    print("[SYSTEM] Allocating memory and booting Neural Networks...")
    ai_summarizer=summarizer.initialize_summarizer()
    ai_ner=ner_extractor.initialize_ner()
    print("[SYSTEM] All AI Models successfully loaded into RAM.\n")
    print("[PIPELINE] Stage 1: Compressing raw reports into tactical summaries...")
    summarized_data=summarizer.summarize_events(clean_events_list, ai_summarizer)
    print("[PIPELINE] Stage 2: Extracting target entities (WHO and WHERE)...")
    final_intelligence=ner_extractor.extract_entities(summarized_data, ai_ner)
    print("\n"+"="*60)
    print("  FINAL TACTICAL BRIEFING")
    print("="*60)
    
    for intel in final_intelligence:
        print(f"\n[ALERT THREAD] {intel['report_title']}")
        print(f"AI SUMMARY:    {intel['ai_summary']}")
        print(f"LOCATIONS:     {intel.get('locations_spotted', [])}")
        print(f"ORGANIZATIONS: {intel.get('organizations_involved', [])}")
        print(f"KEY PEOPLE:    {intel.get('key_people', [])}")
        print("-"*60)
        
    print("\n[SYSTEM] Pipeline execution complete. Shutting down securely.")

if __name__=="__main__":
    run_intelligence_pipeline()