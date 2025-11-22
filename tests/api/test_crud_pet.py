import time
import allure
from helpers import _payload
from clases.pet import Pet
from clases.allure import Allure
from clases.allure import AllurePet
import logging

pet = Pet()


@allure.story('Получение питомцев по категории')
@allure.title('GET-запрос на получение питомцев с рандомным статусом')
def test_get_pets(url_api, _payload):
    params = {"status": _payload['status']}
    response = pet.get_pets(url_api + '/findByStatus', params=params)
    Allure.logining_allure_response_json(result=response, name="Response body")  # логирование response в allure
    logging.info( f"Method: GET, URL: {response.url}, Status: {response.status_code}, Params: {params}")  # логирование в консоль
    assert response.status_code == 200


@allure.story('Получение питомца по его id')
@allure.title('GET-запрос на получение определенного питомца по его id')
def test_get_pet_id(url_api, _payload):
    with allure.step('Создаем питомца и получаем его id'):
        Allure.logining_allure_request_json(request_body=_payload, name='Request')
        response_post_pet = pet.create_pet(url=url_api, payload=_payload)
        logging.info(f"Method: POST, URL: {response_post_pet.url}, Status: {response_post_pet.status_code}")  # логирование в консоль
        id_new_pet = response_post_pet.json()['id']
        Allure.logining_allure_response_json(response_post_pet, name="Response")  # логирование response в allure
    with allure.step('Добавляем в get-запрос id созданного питомца'):
        response = pet.get_pet_id(url=url_api, id_pet=id_new_pet)
        logging.info(f"Method: GET, URL: {response.url}, Status: {response.status_code}")  # логирование в консоль
        Allure.logining_allure_response_json(response, name="Response")  # логирование response в allure
    assert response.status_code == 200
    assert response.json()['name'] == _payload['name']
    #time.sleep(10)  ## слипаю, так как API-сервис нестабилен и может не учитывать передаваемые параметры, если метод создания вызывается несколько раз подряд


@allure.story('Создание питомца')
@allure.title('Создаем питомца и проверяем, что питомец создался корректно.')
def test_post_create_pet(url_api, _payload):
    ## Важно! Запрос на создание питомца иногда может падать - API-сервис нестабилен и иногда может игнорировать
    # передаваемые параметры (если отправить запрос на создание питомца несколько раз подряд).
    with allure.step('Создаем питомца'):
        Allure.logining_allure_request_json(request_body=_payload, name='Request')
        response_post_pet = pet.create_pet(url=url_api, payload=_payload)
        logging.info(f"Method: POST, URL: {response_post_pet.url}, Status: {response_post_pet.status_code}")  # логирование в консоль
        Allure.logining_allure_response_json(response_post_pet, name="Response")  # логирование response в allure
        name_pet = response_post_pet.json()['name']  ## получаем имя питомца и потом его ассертим
    with allure.step('Получаем id созданного питомца и передаем его в get-запроc.'):
        id_new_pet = response_post_pet.json()['id']
        response_get_pet = pet.get_pet_id(url=url_api, id_pet=id_new_pet)
        logging.info(f"Method: GET, URL: {response_get_pet.url}, Status: {response_get_pet.status_code}")  # логирование в консоль
        Allure.logining_allure_response_json(response_get_pet, name="Response")  # логирование response в allure
    with allure.step('Получаем имя питомца в get-запросе.'):
        upd_name_pet = response_get_pet.json()['name']
    assert upd_name_pet == name_pet
    with allure.step('Удаляем созданного питомца'):
        delete_new_pet = pet.delete_pet(url=url_api, id_pet=id_new_pet)
        logging.info(f"Method: DELETE, URL: {delete_new_pet.url}, Status: {delete_new_pet.status_code}")  # логирование в консоль
        AllurePet.allure_logining_delete_pet(id_pet=id_new_pet, result=delete_new_pet, name='Response')
    #time.sleep(10)  ## слипаю, так как API-сервис нестабилен и может не учитывать передаваемые параметры, если метод создания вызывается несколько раз подряд


@allure.story('Изменение параметров питомца')
@allure.title('Создаем питомца и меняем его имя.')
def test_update_pet(url_api, _payload):
    ## Важно! Запрос на создание питомца иногда может падать - API-сервис нестабилен и иногда может игнорировать
    # передаваемые параметры (если отправить запрос на создание питомца несколько раз подряд).
    with allure.step('Создаем питомца'):
        Allure.logining_allure_request_json(request_body=_payload, name='Request')
        response_post_pet = pet.create_pet(url=url_api, payload=_payload)
        logging.info(f"Method: POST, URL: {response_post_pet.url}, Status: {response_post_pet.status_code}")  # логирование в консоль
        Allure.logining_allure_response_json(response_post_pet, name="Response")  # логирование response в allure
        #time.sleep(10)  ## слипаю, так как API-сервис нестабилен и может не учитывать передаваемые параметры, если метод создания вызывается несколько раз подряд
    with allure.step('Получаем id созданного питомца, передаем его в PUT-запрос'):
        id_new_pet = response_post_pet.json()['id']
        update_data = {"name": 'AQA'}
        response_put_pet = pet.update_pet(url=url_api, id_pet=id_new_pet, data=update_data)
        logging.info(f"Method: PUT, URL: {response_put_pet.url}, Status: {response_put_pet.status_code}")  # логирование в консоль
        Allure.logining_allure_response_json(response_put_pet, name="Response")  # логирование response в allure
    with allure.step('Получаем имя питомца и сравниаем его с измененным значением'):
        get_pet = pet.get_pet_id(url_api, id_new_pet)
        name_pet = get_pet.json()['name']
        Allure.logining_allure_response_json(get_pet, name="Response")  # логирование response в allure
        assert response_put_pet.status_code == 200
        assert name_pet == update_data['name']
    with allure.step('Удаляем созданного питомца'):
        delete_new_pet = pet.delete_pet(url=url_api, id_pet=id_new_pet)
        logging.info(f"Method: DELETE, URL: {delete_new_pet.url}, Status: {delete_new_pet.status_code}")  # логирование в консоль
        AllurePet.allure_logining_delete_pet(id_pet=id_new_pet, result=delete_new_pet, name='Response')
        #time.sleep(10)  ## слипаю, так как API-сервис нестабилен и может не учитывать передаваемые параметры, если метод создания вызывается несколько раз подряд


@allure.story('Удаление питомца')
@allure.title('Проверка удаления питомца')
def test_delete_pet(url_api, _payload):
    with allure.step('Создаем питомца и получаем его id'):
        Allure.logining_allure_request_json(request_body=_payload, name='Request')
        response_post_pet = pet.create_pet(url=url_api, payload=_payload)
        logging.info(f"Method: POST, URL: {response_post_pet.url}, Status: {response_post_pet.status_code}")  # логирование в консоль
        Allure.logining_allure_response_json(response_post_pet, name="Response")  # логирование response в allure
        id_new_pet = response_post_pet.json()['id']
    with allure.step('Удаляем созданного питомца'):
        delete_new_pet = pet.delete_pet(url=url_api, id_pet=id_new_pet)
        logging.info("Method: DELETE, URL: {delete_new_pet.url}, Status: {delete_new_pet.status_code}")  # логирование в консоль
        AllurePet.allure_logining_delete_pet(id_pet=id_new_pet, result=delete_new_pet, name='Response')
