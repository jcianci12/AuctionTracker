import requests

url = "https://www.manheim.com.au/damaged-vehicles/search?ManufacturerDescription=&FamilyCodeDescription=&CategoryCodeDescription=Recreation+Vehicles+%26+Marine&StateDescription=&CategoryCode=15&State=&ManufacturerCode=&FamilyCode=&Keywords="

response = requests.get(url)
data = response

# Now you can access the data in the 'data' variable
print(data.text)