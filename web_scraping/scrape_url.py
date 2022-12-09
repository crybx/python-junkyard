import requests

print("Enter the url you want to scrape")
url = input("> ")

r = requests.get(url)

# print all attributes of the response object
attrs = vars(r)
print('\n'.join("%s: %s" % item for item in attrs.items()))
