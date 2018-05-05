from urllib.request import urlopen
import json
import time
from geopy.geocoders import Nominatim

class getsyti:
    token = "YOUR TOKEN VK"
    regionid = "ID REGION" https://vk.com/dev/database.getRegions
    url = "https://api.vk.com/method/database.getCities.json?region_id="+regionid+"&country_id=1&count=200&access_token=" + token + "&v=5.52"
    response = urlopen(url)
    data = response.read()
    jsn = json.loads(data)
    if (jsn["response"]["items"]):
        for st in (jsn["response"]["items"]):
            title = (st["title"])
            id = str(st["id"])
            urlus = "https://api.vk.com/method/users.search.json?city=" + id + "&access_token=" + token + "&v=5.52"
            response2 = urlopen(urlus)
            data2 = response2.read()
            jsn2 = json.loads(data2)

            cnt = str(jsn2["response"]["count"])

            geolocator = Nominatim() #get the coordinates for transfer to the map
            if geolocator.geocode(title):
                location = geolocator.geocode(title)
                adr = (location.address)
                lat = (location.latitude)
                lot = (location.longitude)

                print (title + "," + str(lat) +"," + str(lot) + "," + cnt)
