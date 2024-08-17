from textblob import TextBlob
from newspaper import Article

#text analysis with specified url

url = "https://en.wikipedia.org/wiki/Library"
article = Article(url)
article.download()
article.parse()

text = article.text
print(text)

# Perform sentiment analysis with TextBlob
blob = TextBlob(text)
print(f"Sentiment: {blob.sentiment.polarity}")

#------------------------------------------------------------------
print("------------------------------------------------------------------" )
#text analysis with specified text
with open('t.text' , 'r') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)    
