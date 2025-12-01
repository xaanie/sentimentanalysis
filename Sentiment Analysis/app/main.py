from fastapi import FastAPI
from app.sentiment_chain import analyze_sentiment

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Sentiment Analysis API is running"}

@app.post("/analyze")
def analyze(text: str):
    result = analyze_sentiment(text)
    return {"text": text, "sentiment": result}
