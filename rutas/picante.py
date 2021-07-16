import requests as r
def getPizzasPicante(lang):
    print(lang)
    URL = f'http://localhost:8080/listar?nivel={lang}'
    print(URL)
    data=r.get(URL)
    return data.json()