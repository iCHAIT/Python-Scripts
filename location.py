from geopy.geocoders import Nominatim

geolocator = Nominatim()

lc = "Oregon Coast"  # Replace this with any location you want.

place = geolocator.geocode(lc)
print place.raw
