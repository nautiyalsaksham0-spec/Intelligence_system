import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline

def train_threat_classifier():
    print("[ML ENGINE] Training Custom AI Threat Classifier...")
    training_data=[
        ("Massive influx of armored vehicles and troops crossing border", 2),
        ("Cyber attack compromised northern power grid", 2),
        ("Heavy artillery fire reported near civilian sector", 2),
        ("Unidentified drone spotted hovering near military base", 1),
        ("Border skirmish with light gunfire, no casualties", 1),
        ("Local protests peaceful, crowd dispersing normally", 0),
        ("Diplomatic summit held in Geneva to discuss trade", 0),
        ("New civilian hospital construction completed", 0)
    ]
    df = pd.DataFrame(training_data, columns=["text", "severity"])
    model=make_pipeline(TfidfVectorizer(),RandomForestClassifier(n_estimators=100,random_state=42))
    model.fit(df["text"],df["severity"])
    print("[ML ENGINE] Success: Threat Classifier is trained and ready!\n")
    return model
def classify_events(analyzed_events_list, trained_model):
    print("Initiating Threat Classification...")
    severity_map={0:"LOW",1:"MEDIUM",2:"HIGH"}
    for event in analyzed_events_list:
        text_to_analyze=event['original_details']
        prediction=trained_model.predict([text_to_analyze])[0]
        event['threat_level']=severity_map[prediction]
    print(f"Success: Classified{len(analyzed_events_list)}events!\n")
    return analyzed_events_list
if __name__=="__main__":
    test_data=[
        {
            "report_title":"Border Region Escalation",
            "original_details":"Intelligence analysts have detected a massive influx of armored vehicles and infantry units moving toward the northern border region."
        },
        {
            "report_title":"City Hall Meeting",
            "original_details":"Local politicians met to discuss the new budget for road repairs. The meeting concluded peacefully at 4 PM."
        }
    ]
    ml_model=train_threat_classifier()
    results=classify_events(test_data, ml_model)
    print("--- THREAT ANALYSIS RESULTS ---")
    for res in results:
        print(f"Report:{res['report_title']}")
        print(f"Calculated Threat Level:[{res['threat_level']}]\n")