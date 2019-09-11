# https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson

# Using this JSON feed:
# 1) Identify every earthquake in California from past week,
# 2) List them chronologically (ascending),
# 3) Output in a format resembling the following e.g.:

import urllib.request
import json
import datetime

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

req = urllib.request.Request(url)

r = urllib.request.urlopen(req).read()
data = json.loads(r.decode('utf-8'))

california = list(filter(lambda x : (x["properties"]["place"].find(", CA") != -1), data["features"]))
sorted_california = list(sorted(california, key=lambda x : x["properties"]["time"]))
# print (sorted_california)
for quake in sorted_california:
    print ("{} | {} | Magnitude: {}".format(datetime.datetime.fromtimestamp(quake["properties"]["time"]/1000).isoformat(),quake["properties"]["place"],quake["properties"]["mag"]))
