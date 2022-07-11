import requests

url = input()

r = requests.get(url)
quote = r.json()['content']

print(quote)
