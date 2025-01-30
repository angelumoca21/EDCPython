import requests

x = requests.get('https://api.escuelajs.co/api/v1/categories')
print(x.text)

#json(JavaScriptObjectNotation)