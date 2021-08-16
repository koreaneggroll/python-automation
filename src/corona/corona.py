from covid import *

country = input("Where do you live? ")

print()

covid = Covid()
print(covid.get_status_by_country_name(country))

print()

print(f"This is the data for {country}")