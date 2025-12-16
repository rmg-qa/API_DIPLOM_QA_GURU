import requests
from jsonschema import validate
from schemas.schemas_requests import create_pet, update_pet
from schemas.schemas_response import response_create_pet, get_pet, delete_and_put_pet_schema


class PetApiMethods:
    @staticmethod
    def get_pets(url, params):
        request = requests.get(f'{url}', params=params)
        return request

    @staticmethod
    def get_pet_id(url, id_pet):
        request = requests.get(f'{url}/{id_pet}')
        validate(instance=request.json(), schema=get_pet)
        return request

    @staticmethod
    def create_pet(url, payload):
        validate(instance=payload, schema=create_pet)
        request = requests.post(f'{url}',
                                headers={"accept": 'application/json',
                                         "Content-Type": 'application/json'},
                                json=payload)
        validate(instance=request.json(), schema=response_create_pet)
        return request

    @staticmethod
    def update_pet(url, id_pet, data):
        validate(instance=data, schema=update_pet)
        request = requests.post(f'{url}/{id_pet}',
                                data=data)
        validate(instance=request.json(), schema=delete_and_put_pet_schema)
        return request

    @staticmethod
    def delete_pet(url, id_pet):
        request = requests.delete(f'{url}/{id_pet}', headers={"accept": 'application/json'})
        try:
            validate(instance=request.json(), schema=delete_and_put_pet_schema)
        except:
            print('Один из обязательных параметров питомца не найден')
        return request
