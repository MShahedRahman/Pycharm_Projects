import phonenumbers
from my_phone_number import *
from phonenumbers import geocoder, carrier

import opencage
from opencage.geocoder import OpenCageGeocode

import folium

API_key = 'eb636dd626ea492288e67647b78e54ba'

phone_number = phonenumbers.parse(number)

country_location = geocoder.description_for_number(phone_number, "en")
service_provider = carrier.name_for_number(phone_number, "en")
print(country_location, service_provider)

geocoder = OpenCageGeocode(API_key)
query = str(country_location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 1)
folium.Marker([lat,lng], popup= country_location).add_to(myMap)

myMap.save("myLocation_baba.html")
