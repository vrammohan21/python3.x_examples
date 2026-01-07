""" import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier

#enter phone number along with country code
#Example:+91 77300 78005
number = input("Enter phone number with country code : ")
 
# Parsing String to the Phone number
phoneNumber = phonenumbers.parse(number)
 
# printing the timezone using the timezone module
timeZone = timezone.time_zones_for_number(phoneNumber)
print("timezone : "+str(timeZone))
 
# printing the geolocation of the given number using the geocoder module
geolocation = geocoder.description_for_number(phoneNumber,"en")
print("location : "+geolocation)
 
# printing the service provider name using the carrier module
service = carrier.name_for_number(phoneNumber,"en")
print("service provider : "+service) """
# track location with the map using the phone number
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
 
import folium
from opencage.geocoder import OpenCageGeocode
 
# taking input the phonenumber along with the country code
#Example: +91 77300 78005
number = input("Enter the PhoneNumber with the country code : ")

# Parsing the phonenumber string to convert it into phonenumber format
phoneNumber = phonenumbers.parse(number)
 
# Storing the API Key in the Key variable
#ex-API "45xx61272xxxxd1cb57164b53exxxx"
Key = " Enter your Api" #generate your api https://opencagedata.com/api


 
# Using the geocoder module of phonenumbers to print the Location
yourLocation = geocoder.description_for_number(phoneNumber,"en")
print("Location : "+yourLocation)
 
# Using the carrier module of phonenumbers to print the service provider name
yourServiceProvider = carrier.name_for_number(phoneNumber,"en")
print("service provider : "+yourServiceProvider)
 
# Using opencage to get the latitude and longitude of the location
geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)
 
# Assigning the latitude and longitude values to the lat and lng variables
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
 
# Getting the map for the given latitude and longitude
myMap = folium.Map(loction=[lat,lng],zoom_start = 9)
 
# Adding a Marker on the map to show the location name
folium.Marker([lat,lng],popup=yourLocation).add_to(myMap)
 
# save map to html file to open it and see the actual location in map format
myMap.save("Location.html")