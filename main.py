import requests
import os
from send_email import send_email

topic = "tesla"

api_key = os.getenv("NEWS_API_KEY")
url = "https://newsapi.org/v2/everything?"\
      f"q={topic}&"\
      "sortBy=publishedAt&"\
      f"apiKey={api_key}&language=en"

# Make Request
response = requests.get(url)
# Get a dictionary with data
content = response.json()
# Access the article titles and description
message = ""
for article in content["articles"][:20]:
    if article["title"] and article["description"]:
        message = "Subject: Today's news" + "\n" \
                  + message + article["title"] + "\n"\
                  + article["description"] + "\n"\
                  + article["url"] + 2*"\n"

send_email(message.encode("utf-8"))
