import requests

url_base = 'https://restful-booker.herokuapp.com'

def cadastrar_usuario():
    endpoint = '/auth'
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url_base + endpoint, json=payload)
    token = response.json()['token']
    return token

token = cadastrar_usuario()
print("Token de autenticação:", token)


def cadastrar_livro(token):
    endpoint = '/booking'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'Basic {token}'}
    payload = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {"checkin": "2023-01-01", "checkout": "2023-01-10"},
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url_base + endpoint, json=payload, headers=headers)
    return response.json()

livro_cadastrado = cadastrar_livro(token)
print("Livro cadastrado:", livro_cadastrado)

def consultar_livro(id_livro, token):
    endpoint = f'/booking/{id_livro}'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'Basic {token}'}
    response = requests.get(url_base + endpoint, headers=headers)
    return response.json()

id_livro = livro_cadastrado['bookingid']
livro_consultado = consultar_livro(id_livro, token)
print("Livro consultado:", livro_consultado)
