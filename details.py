import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileno = input("Enter mobile number with country code : ")
mobileno = phonenumbers.parse(mobileno)

#get timezone a phone number
print(timezone.time_zones_for_number(mobileno))

#getting carrier of a phone number
print(carrier.name_for_number(mobileno, "en"))

#getting region information

print(geocoder.description_for_number(mobileno, "en"))

#validating a phone number
print("valid mobile number:", phonenumbers.is_valid_number(mobileno))

#checking possibility of a number
print("checking possibility of number:", phonenumbers.is_possible_number(mobileno))

