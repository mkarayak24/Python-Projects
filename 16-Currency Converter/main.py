from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.freecurrencyapi.com/"
API_KEY = "fca_live_8q7qijhtnsIiFkqmS44zLXRYVCHrBNLN9m4bYZGh"

printer = PrettyPrinter()

def get_currencies():
    endpoint = f"v1/latest?apikey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()["data"]
    data = list(data.items())
    return data

def print_currencies(currencies):
    for name, value in currencies:
        print(f"{name}-{value}")

def exchange_rate (currency1, currency2):
    endpoint = f"v1/latest?apikey={API_KEY}&currencies={currency2}&base_currency={currency1}"
    url = BASE_URL + endpoint
    response = get(url)
    data = response.json()["data"]
    rate = list(data.values())[0]
    print (f"{currency1} -> {currency2} = {rate}")
    return rate

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return
    try:
        amount = float (amount)
    except:
        print("Invalid amount")

    converted_amount = rate * amount
    print (f"{amount} {currency1} = {converted_amount} {currency2}")
    return converted_amount
    
def main():
    print("Welcome to the currency converter!")
    print("List - lists the different cuurencies")
    print("Convert - convert from one curreny to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            data = get_currencies()
            print_currencies(data)
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = input (f"Enter an amount in {currency1}: ").upper()
            currency2 = input(f"Enter a currency to convert to {currency1}: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input(f"Enter a currency to convert to {currency1}: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print ("Unrecognized command :(")

main()

