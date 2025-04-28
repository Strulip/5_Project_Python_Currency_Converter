import requests
import json


def get_currency_input():
    return input("Enter the currency that you want to receive:\n").lower()


def get_amount_input():
    return float(input("Enter the amount that must be converted:\n"))


def start_calculator(uc, udc, uac):
    while True:

        if uc.isdigit() or len(uc) != 3:
            uc = input("Please enter the existing currency in the format 'XXX' (Latin letters):\n").lower()
            continue

        if udc.isdigit() or len(udc) != 3:
            udc = input("Please enter the desired currency in the format 'XXX' (Latin letters):\n").lower()
            continue

        print("Checking the cache...")

        if udc in rates_cached:
            print('Oh! It is in the cache!')
            print(convert_amount(udc, uac))

        else:
            print('Sorry, but it is not in the cache!')
            get_rate(uc, udc)
            print(convert_amount(udc, uac))

        udc = input(
            "\nIf you want to exit the program, enter 'exit'\n"
            "If you want to change the currency you have, enter 'change' or 'switch'\n"
            "Enter the currency that you want to receive:\n"
        ).lower()

        if udc == '' or udc == 'exit':
            break

        if udc in ['change', 'switch']:
            rates_cached.clear()
            uc = input("Enter the currency that you have:\n").lower()
            preload(uc, preload_list)
            udc = get_currency_input()
            uac = get_amount_input()
            continue

        uac = get_amount_input()


def get_rate(uc, udc):
    while True:
        request_json = requests.get(f"http://www.floatrates.com/daily/{uc}.json")

        if request_json.status_code >= 400:
            uc = input("The currency that you have does not exist.\nPlease try again:\n").lower()
            continue

        request = json.loads(request_json.text)

        if udc in request:
            rates_cached[udc] = request[udc]
            break
        else:
            udc = input("The currency that you want does not exist.\nPlease try again:\n").lower()


def preload(uc, pl):
    while True:
        request_json = requests.get(f"http://www.floatrates.com/daily/{uc}.json")

        if request_json.status_code >= 400:
            uc = input("The currency that you have does not exist.\nPlease try again:\n").lower()
            continue

        request = json.loads(request_json.text)

        for key, value in request.items():
            if key in pl:
                rates_cached[key] = value

        break


def convert_amount(udc, uac):
    rate = rates_cached.get(udc, {}).get('rate')
    if rate is None:
        return "Conversion error: rate not found."
    return f'You received {uac * rate:.2f} {udc.upper()}.'


# Global cache
rates_cached = {}

preload_list = ['eur', 'usd']

user_currency = input("Enter the currency that you have:\n").lower()
preload(user_currency, preload_list)
user_desired_currency = input("Enter the currency that you want to receive:\n").lower()
user_amount_currency = float(input("Enter the amount that must be converted:\n"))
start_calculator(user_currency, user_desired_currency, user_amount_currency)
















