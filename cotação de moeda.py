import httpx

base_currency = input('Digite a mode de base: ').upper()
currency = input('Digite a moeda desejada: ').upper()

response = httpx.get(
    url=f'https://api.exchangerate.host/lastest?base={base_currency}'
).json()
currency_data + response['rates']

print(f'1 {base_currency} vale {currency_data.get(currency)} {currency}')