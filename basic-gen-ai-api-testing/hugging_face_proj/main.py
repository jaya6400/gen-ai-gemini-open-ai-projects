from transformers import pipeline

# For text generation with distilgpt2
text_generator = pipeline("text-generation", model="distilbert/distilgpt2")
print(text_generator("Hello, I am a language model and I can"))

# For sentiment analysis
sentiment_classifier = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
print(sentiment_classifier("I love using Hugging Face models!"))