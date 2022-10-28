import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Please enter your expected phone number with country code: ")
phone = phonenumbers.parse(number)

time = timezone.time_zones_for_number(phone)
time1 = timezone.time_zones_for_geographical_number(phone)
carrier_variable = carrier.name_for_number(phone, "en")


registration_mat = geocoder.description_for_number(phone, "en")

print(phone)
print(time1, carrier_variable,registration_mat)








