import phonenumbers as p
from phonenumbers import timezone as t
from phonenumbers import geocoder, carrier as g,c
unknown = p.parse("+919193560690")
timeZone = t.time_zones_for_number(unknown)
# This will print the phone number and 
# it's basic details.
print(unknown)
print(timeZone)