import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from test import number

country_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(country_number, "en"))

print(geocoder)

service_provider = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_provider, "en"))








