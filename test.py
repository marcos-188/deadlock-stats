# import http.client
#
# conn = http.client.HTTPSConnection("assets.deadlock-api.com")
#
# conn.request("GET", "/v2/heroes?language=english&client_version=6484&only_active=true")
#
# response = conn.getresponse()
# print(response.read().decode())
#
# conn.close()

# import http.client
#
# conn = http.client.HTTPSConnection("assets.deadlock-api.com")
#
# conn.request("GET", "/v1/icons?client_version=6484")
#
# response = conn.getresponse()
# print(response.read().decode())
#
# conn.close

# from stats_module import pobierz_gry
#
# print(pobierz_gry(5,255762123,0)[0])

import requests
import json

from stats_module import pobierz_postacie

print(pobierz_postacie())