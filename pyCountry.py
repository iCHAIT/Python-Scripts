import pycountry

countr = {}

t = list(pycountry.countries)

for country in t:
    countr[country.alpha2] = country.name

print countr
