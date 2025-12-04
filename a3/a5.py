import requests



url = "https://api.restful-api.dev/objects"
res = requests.get(url).json()


print(len(res))
print(res[0])