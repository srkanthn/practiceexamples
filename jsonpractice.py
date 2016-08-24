from urllib import request
import json
import codecs



#
# url='http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson'
#
# def main():
#     str='{"type":"FeatureCollection","metadata":{"generated":1471971620000,"url":"http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson","title":"USGS Magnitude 2.5+ Earthquakes, Past Hour","status":200,"api":"1.5.2","count":1},"features":[{"type":"Feature","properties":{"mag":2.6,"place":"14km SW of Tok, Alaska","time":1471969581000,"updated":1471970258072,"tz":-480,"url":"http://earthquake.usgs.gov/earthquakes/eventpage/ak13874179","detail":"http://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak13874179.geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"automatic","tsunami":0,"sig":104,"net":"ak","code":"13874179","ids":",ak13874179,","sources":",ak,","types":",general-link,geoserve,origin,","nst":null,"dmin":null,"rms":1.13,"gap":null,"magType":"ml","type":"earthquake","title":"M 2.6 - 14km SW of Tok, Alaska"},"geometry":{"type":"Point","coordinates":[-143.2209,63.2622,15]},"id":"ak13874179"}]}'
#     json_data=json.loads(str,encoding='utf-8')
#     print(json_data)
#     for i in json_data['features']:
#         # print(i)
#         print(i['properties']['place'])
#         print(i['properties']['felt'])
#         print(i['properties']['mag'])
#
# if __name__== '__main__':
#     main()

# import pprint
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
#
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
#
# pprint.pprint(count)

a=['a','A','b','B','c','C','d','D']
a.sort(reverse=True,key=str.upper)
print(a)