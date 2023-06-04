import requests

api_key = "6dbbcbf354eb4fceac2f3b6f878aa7f3"
url = f"https://newsapi.org/v2/everything?q=tesla&"\
      f"from=2023-05-04&sortBy=publishedAt&"\
      f"apiKey={api_key}"

# Make Request
request = requests.get(url)
# Get a dictionary with data
content = request.json()
# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
