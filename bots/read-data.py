import requests
url = 'https://api.jsonbin.io/v3/b/63eae006c0e7653a0576f666/latest'
headers = {
  'X-Master-Key': '$2b$10$8ZLGc53IHdU2svwoocfXF.qh1P7GfegPE5F7oGskVjAg.ji1qTNXa'
}

req = requests.get(url, json=None, headers=headers)
data = req.json()
cleaning = data['record']
first_value = list(cleaning.values())[0]
for value, key in cleaning:
    print(value, key)

