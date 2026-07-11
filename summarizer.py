from transformers import pipeline
import transformers
transformers.logging.set_verbosity_error()
def initialize_summarizer():
    print("Loading AI Summarization Model(This might take a minute the first time)")
    summarizer=pipeline("summarization",model="sshleifer/distilbart-cnn-12-6")
    return summarizer

def summarize_events(clean_events_list, summarizer):
    print("Initiating AI Summarization Pipeline...")
    analyzed_events=[]

    for event in clean_events_list:
        text_to_summarize=event['details']
        if len(text_to_summarize.split())>20:
            summary_output=summarizer(text_to_summarize,max_length=50,min_length=10,do_sample=False)
            final_summary=summary_output[0]['summary_text']
        else:
            final_summary=text_to_summarize
        analyzed_events.append({
            "report_title": event['report_title'],
            "original_details": text_to_summarize,
            "ai_summary": final_summary
        })
        
    print(f"Success: AI Summarized {len(analyzed_events)} events!\n")
    return analyzed_events
if __name__ == "__main__":
    test_data=[
        {
            "report_title":"Heavy Troop Movement Spotted",
            "details":"Intelligence analysts have detected a massive influx of armored vehicles and infantry units moving toward the northern border region over the last 48 hours. Satellite imagery confirms the establishment of temporary forward operating bases. Local sources report restricted civilian movement and disrupted communication lines in the area."
        }
    ]
    ai_model=initialize_summarizer()
    results=summarize_events(test_data, ai_model)
    print("ORIGINAL REPORT")
    print(results[0]['original_details'])
    print("\nAI SUMMARY")
    print(results[0]['ai_summary'])