import os

import dotenv
import allure
import pytest
from classes.allure_attach import AllurePetLoggingMethods
from classes.allure_attach import AllureLoggingMethods
from classes.pet_api_methods import PetApiMethods
from tests import helpers

pet = PetApiMethods()
dotenv.load_dotenv()
base_url = os.getenv('URL')


@allure.story('Получение питомцев по определенному статусу: "available", "pending", "sold"')
@allure.title('Получение питомцев по статусу')
@allure.tag('api')
@pytest.mark.parametrize('status', ["available", "pending", "sold"])
def test_get_pets_by_status(status):
    params = {"status": status}
    response = pet.get_pets(base_url + '/findByStatus', params=params)
    AllureLoggingMethods.logging_response_json(result=response, name="Response body")
    helpers.log_2_console(response, params)
    assert response.status_code == 200
    assert response.json()[0]['status'] == status


@allure.story('Получение питомца по его id')
@allure.title('GET-запрос на получение определенного питомца по его id')
@allure.tag('api')
def test_get_pet_by_id(generate_payload):
    with allure.step('Создаем питомца и получаем его id'):
        AllureLoggingMethods.logging_request_json(request_body=generate_payload, name='Request')
        response = pet.create_pet(url=base_url, payload=generate_payload)
        helpers.log_2_console(response)
        id_new_pet = response.json()['id']
        AllureLoggingMethods.logging_response_json(response, name="Response")
    with allure.step('Получаем созданного питомца по его id'):
        response = pet.get_pet_id(url=base_url, id_pet=id_new_pet)
        helpers.log_2_console(response)
        AllureLoggingMethods.logging_response_json(response, name="Response")
    assert response.status_code == 200
    assert response.json()['name'] == generate_payload['name']


@allure.story('Создание питомца')
@allure.title('Создаем питомца и проверяем, что питомец создался корректно.')
@allure.tag('api')
def test_create_pet(generate_payload):
    with allure.step('Создаем питомца'):
        AllureLoggingMethods.logging_request_json(request_body=generate_payload, name='Request')
        response_create_pet = pet.create_pet(url=base_url, payload=generate_payload)
        helpers.log_2_console(response_create_pet)
        AllureLoggingMethods.logging_response_json(response_create_pet, name="Response")
        pet_name = response_create_pet.json()['name']  ## получаем имя питомца и потом его ассертим
    with allure.step('Получаем созданного питомца по его id'):
        id_new_pet = response_create_pet.json()['id']
        response_getting_a_created_pet = pet.get_pet_id(url=base_url, id_pet=id_new_pet)
        helpers.log_2_console(response_getting_a_created_pet)
        AllureLoggingMethods.logging_response_json(response_getting_a_created_pet, name="Response")
    with allure.step('Получаем имя созданного питомца'):
        upd_pet_name = response_getting_a_created_pet.json()['name']
    assert response_create_pet.status_code == 200
    assert response_getting_a_created_pet.status_code == 200
    assert upd_pet_name == pet_name
    with allure.step('Удаляем созданного питомца'):
        delete_created_pet = pet.delete_pet(url=base_url, id_pet=id_new_pet)
        helpers.log_2_console(delete_created_pet)
        AllurePetLoggingMethods.logging_delete_pet(id_pet=id_new_pet, result=delete_created_pet, name='Response')
    assert delete_created_pet.status_code == 200


@allure.story('Изменение параметров питомца')
@allure.title('Создаем питомца и меняем его имя.')
@allure.tag('api')
def test_update_pet(generate_payload):
    with allure.step('Создаем питомца'):
        AllureLoggingMethods.logging_request_json(request_body=generate_payload, name='Request')
        response_create_pet = pet.create_pet(url=base_url, payload=generate_payload)
        helpers.log_2_console(response_create_pet)
        AllureLoggingMethods.logging_response_json(response_create_pet, name="Response")
    with allure.step('Получаем id созданного питомца, передаем его в PUT-запрос'):
        id_new_pet = response_create_pet.json()['id']
        update_data = {"name": 'AQA'}
        response_update_created_pet = pet.update_pet(url=base_url, id_pet=id_new_pet, data=update_data)
        helpers.log_2_console(response_update_created_pet)
        AllureLoggingMethods.logging_response_json(response_update_created_pet, name="Response")
    with allure.step('Получаем имя питомца и сравниаем его с измененным значением'):
        response_getting_a_created_pet = pet.get_pet_id(base_url, id_new_pet)
        pet_name = response_getting_a_created_pet.json()['name']
        helpers.log_2_console(response_getting_a_created_pet)
        AllureLoggingMethods.logging_response_json(response_getting_a_created_pet, name="Response")
        assert response_getting_a_created_pet.status_code == 200
        assert pet_name == update_data['name']
    with allure.step('Удаляем созданного питомца'):
        delete_created_pet = pet.delete_pet(url=base_url, id_pet=id_new_pet)
        helpers.log_2_console(delete_created_pet)
        AllurePetLoggingMethods.logging_delete_pet(id_pet=id_new_pet, result=delete_created_pet, name='Response')
        assert delete_created_pet.status_code == 200


@allure.story('Удаление питомца')
@allure.title('Проверка удаления питомца')
@allure.tag('api')
def test_delete_pet(generate_payload):
    with allure.step('Создаем питомца и получаем его id'):
        AllureLoggingMethods.logging_request_json(request_body=generate_payload, name='Request')
        response_create_pet = pet.create_pet(url=base_url, payload=generate_payload)
        helpers.log_2_console(response_create_pet)
        AllureLoggingMethods.logging_response_json(response_create_pet, name="Response")
        id_new_pet = response_create_pet.json()['id']
    with allure.step('Удаляем созданного питомца'):
        delete_created_pet = pet.delete_pet(url=base_url, id_pet=id_new_pet)
        helpers.log_2_console(delete_created_pet)
        AllurePetLoggingMethods.logging_delete_pet(id_pet=id_new_pet, result=delete_created_pet, name='Response')
        assert delete_created_pet.status_code == 200
        assert delete_created_pet.json()['type'] == 'unknown'
    with allure.step('Проверяем, что питомец точно удалился'):
        repeat_the_deletion_of_the_created_pet = pet.delete_pet(url=base_url, id_pet=id_new_pet)
        helpers.log_2_console(repeat_the_deletion_of_the_created_pet)
        assert repeat_the_deletion_of_the_created_pet.status_code == 404
