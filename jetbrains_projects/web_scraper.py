import requests

url = input()
# url = "http://api.quotable.io/quotes/-4WQ_JwFWI"
# url = "http://api.quotable.io/asdfgh"

r = requests.get(url)

if r:
    try:
        quote = r.json()['content']
        print(quote)
    except KeyError:
        print("Invalid quote resource!")
else:
    print("Invalid quote resource!")

