import requests

url = "https://24nxpvemp7t7kk2ejbhwhquciu0faoiu.lambda-url.us-east-1.on.aws/"
payload = {
    'reel_url': 'https://www.instagram.com/p/DSKilXBDeyq/'
}

response = requests.post(url, json=payload)
data = response.json()
print(data)