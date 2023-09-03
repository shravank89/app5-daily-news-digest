import requests as re
from send_email import send_email


API_KEY = "d7bf198e298449c287b65b182fcd58dc"

url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"

# Make Requests
request = re.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
data = ""
for article in content["articles"]:
    if article["title"] is not None \
            and article["url"] is not None \
            and article["description"] is not None \
            and article["url"] != "https://removed.com":
        data = data + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

data = "Subject: Top 20 News: India" + "\n" + data
send_email(data.encode('utf-8'))


