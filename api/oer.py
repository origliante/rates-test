import requests

APP_ID = 'c4789b28f9dc4487a1af4ce27605672a'

def get_currencies():
    payload = {'app_id': APP_ID}
    return requests.get('https://openexchangerates.org/api/currencies.json', params=payload, timeout=5)
