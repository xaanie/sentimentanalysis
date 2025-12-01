# Sentiment Analysis API (LangChain + FastAPI + Docker)

This project provides a simple web API that analyzes the sentiment of a given text using LangChain and an LLM. It returns a JSON output with the sentiment (positive, negative, or neutral) and a brief explanation.

---

 Features

- LangChain + LLM sentiment analysis
- FastAPI endpoint: `/analyze-sentiment`
- JSON structured output
- Dockerized for easy deployment
- Fully tracked with Git

---

  How It Works

1. User sends text to `/analyze-sentiment`
2. LangChain prompts an LLM to evaluate sentiment
3. The LLM returns JSON with:
   - sentiment
   - explanation

---

## 📦 Installation (Local)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Xaanie/sentiment-api.git
cd sentiment-api
