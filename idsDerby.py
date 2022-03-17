import requests
url = "https://opendomesday.org/api/1.0/county/"
r = requests.get(url)
data = r.json()
for i in data:
    if i.get('name') == "Derbyshire":
        place = i.get("places_in_county")
        for j in place:
           print(j.get("id"))


