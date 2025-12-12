import requests

url = "https://6tbypxrnfjxfwzthmahds52oky0hpuhc.lambda-url.us-east-1.on.aws/"
payload = {
    'reel_url': 'https://www.instagram.com/p/DQzJhVck713/'
}

response = requests.post(url, json=payload)
data = response.json()
print(data)