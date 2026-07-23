from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import ingest
import summarizer
import ner_extractor
import classifier
app=FastAPI(
    title="AI-TIES Tactical Intelligence API",
    description="Backend service for live AI news summarization,NER,and threat classification.",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
print("\n" + "="*60)
print("BOOTING AI-TIES ENGINE & LOADING MODELS INTO RAM")
print("="*60)
ai_summarizer=summarizer.initialize_summarizer()
ai_ner=ner_extractor.initialize_ner()
ml_classifier=classifier.train_threat_classifier()
print("[SYSTEM] ALL AI MODELS LOADED & READY FOR WEB TRAFFIC!")
print("="*60+"\n")
@app.get("/")
def root():
    return {
        "status":"online",
        "system":"AI-TIES Tactical Intelligence Engine",
        "version":"1.0.0"
    }
@app.get("/api/intel")
def get_tactical_intelligence():
    """
    Main API endpoint:
    1. Fetches live breaking BBC news via ingest.py
    2. Runs transformer-based summarization
    3. Extracts named entities (Locations, Orgs, People)
    4. Predicts threat levels (HIGH / LOW) via ML classifier
    5. Returns structured JSON
    """
    print("\n[API] Received request for live intelligence feed...")
    clean_events_list=ingest.fetch_live_events()
    if not clean_events_list:
        return {"status":"error","message":"Failed to fetch live feed data.","data":[]}
    summarized_data=summarizer.summarize_events(clean_events_list,ai_summarizer)
    ner_data=ner_extractor.extract_entities(summarized_data,ai_ner)
    final_intelligence=classifier.classify_events(ner_data,ml_classifier)
    return{
        "status":"success",
        "count":len(final_intelligence),
        "data":final_intelligence
    }