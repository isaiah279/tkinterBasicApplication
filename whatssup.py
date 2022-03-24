

import phonenumbers
import requests
from file_two import number


from phonenumbers import is_number_geographical
from phonenumbers import geocoder
from phonenumbers import carrier


from phonenumbers import carrier
servic_number=phonenumbers.parse(number,"Ro")
print(carrier.name_for_number(servic_number,'en'))
ch_number = phonenumbers.parse(number, "CH")  # c=county,h-history
print(geocoder.description_for_number(ch_number, 'en'))

