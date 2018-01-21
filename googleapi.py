# -*- coding: utf-8 -*-

import json
import urllib

api_key = 'google_api_key'
google_api_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
address = 'Jungstrasse 5, Zurigo'
params = {'key': api_key, 'address': address}

params_encode = urllib.urlencode(params)

#print params_encode  # key=google_api_key&address=Jungstrasse+5%2C+Zurigo

#url = google_api_url + params_encode
#req = urllib.urlopen(url)
#j_data = req.read()

j_data = '''{
   "results" : [
      {
         "address_components" : [
            {
               "long_name" : "5",
               "short_name" : "5",
               "types" : [ "street_number" ]
            },
            {
               "long_name" : "Jungstrasse",
               "short_name" : "Jungstrasse",
               "types" : [ "route" ]
            },
            {
               "long_name" : "Kreis 11",
               "short_name" : "Kreis 11",
               "types" : [ "political", "sublocality", "sublocality_level_1" ]
            },
            {
               "long_name" : "Zürich",
               "short_name" : "Zürich",
               "types" : [ "locality", "political" ]
            },
            {
               "long_name" : "Zürich",
               "short_name" : "Zürich",
               "types" : [ "administrative_area_level_2", "political" ]
            },
            {
               "long_name" : "Zürich",
               "short_name" : "ZH",
               "types" : [ "administrative_area_level_1", "political" ]
            },
            {
               "long_name" : "Switzerland",
               "short_name" : "CH",
               "types" : [ "country", "political" ]
            },
            {
               "long_name" : "8050",
               "short_name" : "8050",
               "types" : [ "postal_code" ]
            }
         ],
         "formatted_address" : "Jungstrasse 5, 8050 Zürich, Switzerland",
         "geometry" : {
            "location" : {
               "lat" : 47.4147239,
               "lng" : 8.5449231
            },
            "location_type" : "ROOFTOP",
            "viewport" : {
               "northeast" : {
                  "lat" : 47.4160728802915,
                  "lng" : 8.546272080291502
               },
               "southwest" : {
                  "lat" : 47.4133749197085,
                  "lng" : 8.543574119708497
               }
            }
         },
         "place_id" : "ChIJBbqiPIUKkEcRY0uBfNUlnEQ",
         "types" : [ "street_address" ]
      }
   ],
   "status" : "OK"
}
'''
data = json.loads(j_data)

if data['status'] != 'OK':
    print('Error in the responce')
    quit()

#print data['results']
# result is a list, so I take the first element with [0] and then I search the key in the dictionary
print data['results'][0]['geometry']['location']['lat'], data['results'][0]['geometry']['location']['lng']
