import requests
[[print(j.get("id")) for j in i.get("places_in_county")] for i in requests.get("https://opendomesday.org/api/1.0/county/").json() if i.get('name') == "Derbyshire"]
