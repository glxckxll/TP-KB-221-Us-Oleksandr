import requests

def get_exchange_rate(currency_code):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json&valcode={currency_code}"
    resp = requests.get(url)

    if resp.status_code == 200:
        base = resp.json()
        if base:
            return base[0]["rate"]
    return None

def get_currencies_starting_with(letter):
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json"
    resp = requests.get(url)

    if resp.status_code == 200:
        base = resp.json()
        codes = [entry["cc"] for entry in base if entry["cc"].startswith(letter.upper())]
        return codes
    return []

print("Інформація про найпопулярніші курси валют:")
for code in ["EUR", "USD", "PLN"]:
    rate = get_exchange_rate(code)
    print(f"1 {code} = {rate} UAH")


while True:
    user_input = input("Введіть перший символ коду валюти (наприклад, E, або 'Q' для виходу): ").upper()

    if user_input == "Q":
        print("Вихід")
        break

    codes = get_currencies_starting_with(user_input)

    if not codes:
        print("Немає валют, які починаються з введеного символу.")
        continue

    print("Доступні коди валют:")
    for code in codes:
        print(code)

    currency_code = input("Введіть код валюти: ").upper()

    if currency_code not in codes:
        print("Невірний код валюти. Спробуйте ще раз або введіть 'Q' для виходу.")
        continue

    while True:
        try:
            amount = float(input("Введіть суму для конвертації: "))
            break
        except ValueError:
            print("Було введено невірне значення")

    rate = get_exchange_rate(currency_code)

    if rate is not None:
        money = amount * rate
        print(f"{amount} {currency_code} = {money} UAH")
    else:
        print("Не вдалося отримати курс валюти")
