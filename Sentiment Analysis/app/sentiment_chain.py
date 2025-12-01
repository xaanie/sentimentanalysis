def analyze_sentiment(text: str) -> str:
    text = text.lower()

    positive_words = ["good", "great", "excellent", "amazing", "happy", "love"]
    negative_words = ["bad", "terrible", "awful", "sad", "hate"]

    score = 0

    for word in positive_words:
        if word in text:
            score += 1

    for word in negative_words:
        if word in text:
            score -= 1

    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    else:
        return "neutral"
