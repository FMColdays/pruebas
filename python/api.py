import requests

i = 1
while i < 20:
    url = "https://jsonplaceholder.typicode.com/posts"
    peticion = requests.get(url)
    respuesta = peticion.json()
    if respuesta[i]['userId'] == 2:
        id = respuesta[i]['id']
        print('El id es {}'.format(id))
    i += 1






