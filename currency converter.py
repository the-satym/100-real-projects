import requests
from dotenv import load_dotenv
import os

load_dotenv("keys.env")

# Currency Converter using ExchangeRate-API
from_currency = input("Enter the currency code you want to convert from (e.g., USD): ").upper().strip()
to_currency = input("Enter the currency code you want to convert to (e.g., EUR): ").upper().strip()
amount = float(input(f"Enter the amount in {from_currency} you want to convert: "))


api = os.getenv("currency_key")
r= requests.get(api+from_currency)

data = r.json()
rates = data.get('conversion_rates',{})

last_updated = data.get('time_last_update_utc')

if to_currency in rates:
    converted_amount = amount * rates[to_currency]

    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}.")
else:
    print(f"Conversion rate for {to_currency} not found.")
    print("Please check the currency code and try again.")

print(f'suggested currencies: {amount} {from_currency} = {rates.get('USD',) * amount} USD' if to_currency != "USD" else "" )
print(f'suggested currencies: {amount} {from_currency} = {rates.get('EUR',) * amount} EUR' if to_currency != "EUR" else "" )
print(f'suggested currencies: {amount} {from_currency} = {rates.get('JPY',) * amount} JPY' if to_currency != "JPY" else "" )
print(f'suggested currencies: {amount} {from_currency} = {rates.get('AUD',) * amount} AUD' if to_currency != "AUD" else "" )
print(f'suggested currencies: {amount} {from_currency} = {rates.get('GBP',) * amount} GBP' if to_currency != "GBP" else "" )

print(f'prices last updated at {last_updated} UTC')