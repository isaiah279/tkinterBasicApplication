# currency converter
seling_to_kenya = input("enter sell or buy:")
buy_usa = input("enter string:")

if seling_to_kenya == "sell":
    country_kenya = input("enter amount")
    mouney_kenyer = int(country_kenya)
    print("Ksh", mouney_kenyer * 0.009)
elif buy_usa == "buy":
    country_usa = input("enter $US:")
    us = int(country_usa)
    print("$", us / 110.8)
else:
    print("contact admin")
