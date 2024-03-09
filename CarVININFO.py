# Import Vin function from vininfo using the import function
from vininfo import Vin
# Pass some random VIN number to the Vin() function to create an object
# and store it in a variable
vin_numbr = Vin('MAJGERTYKGHG58025')
print("Vehicle information using VIN number:\n") 
# Apply country attribute on the above vin number to get 
# the country to whcih the vehicle belongs to.
print("Country Name:", vin_numbr.country)     
# Apply manufacturer attribute on the above vin number to get 
# the manufacturer name
print("Manufacturer Name:", vin_numbr.manufacturer)      
# Apply wmi attribute on the above vin number to get 
# the model name
print("Model:", vin_numbr.wmi)   
# Apply vds attribute on the above vin number to get 
# the Plant name
print("Plant:", vin_numbr.vds)
# Apply vis attribute on the above vin number to get 
# the Serial Number
print("Serial Number:", vin_numbr.vis)
# Apply region attribute on the above vin number to get 
# the region name i.e, in which continent the vehicle is manufactured.
print("Region Name: ", vin_numbr.region)
