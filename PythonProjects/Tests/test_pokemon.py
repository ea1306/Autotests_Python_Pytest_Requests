import requests
import pytest

def test_status_code_trainers():
    response = requests.get('https://api.pokemonbattle.me:9104/trainers')
    assert response.status_code == 200

def test_name_trainers():
    response = requests.get('https://api.pokemonbattle.me:9104/trainers',params ={'trainer_id': '2002'} )
    assert response.status_code == 200 

    
@pytest.mark.parametrize('key,value', [('trainer_name','Sara'),('city','moscow'),('level', '1')])

def test_parts_of_answer(key, value):
    response = requests.get('https://api.pokemonbattle.me:9104/trainers', params = {'trainer_id': '2002'})
    assert response.json()[key] == value