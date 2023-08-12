import requests

token = '86d6e699050947518201ef868f722820'

response = requests.post('https://api.pokemonbattle.me:9104/trainers/reg', headers = {'Content-Type': 'application/json',
 'trainer_token':token },
json = {
    "trainer_token": "86d6e699050947518201ef868f722820",
    "email": "oxx3n@sfolkar.com",
    "password": "Iloveqa1"
})
print (response.text)

response = requests.post('https://api.pokemonbattle.me:9104/trainers/confirm_email', headers = {'Content-Type': 'application/json',
 'trainer_token':token },
json = {
    "trainer_token": "86d6e699050947518201ef868f722820"
})
print (response.text)

response = requests.post('https://api.pokemonbattle.me:9104/pokemons', headers = {'Content-Type': 'application/json',
 'trainer_token':token },
json = {
    "name": "Sara",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})
print (response.text)


response_change = requests.put('https://api.pokemonbattle.me:9104/pokemons', headers = {'Content-Type': 'application/json',
 'trainer_token':token },
json = {
    
    "pokemon_id": "6059",
    "name": "Sarra",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})
print (response.text)


response_pokeball = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball',
    headers={'Content-Type': 'application/json', 'trainer_token':token },
    json = {    "pokemon_id": "6059"
            })
print(response_pokeball.text)


