import requests
from send_email import send_email

api_key = "6dbbcbf354eb4fceac2f3b6f878aa7f3"
url = f"https://newsapi.org/v2/everything?q=tesla&"\
      f"from=2023-05-04&sortBy=publishedAt&"\
      f"apiKey={api_key}"

# Make Request
request = requests.get(url)
# Get a dictionary with data
content = request.json()
# Access the article titles and description
message = ""
for article in content["articles"]:
    if article["title"] and article["description"] :
        message = message + article["title"] + "\n" + article["description"] + 2*"\n"

send_email(message.encode("utf-8"))
