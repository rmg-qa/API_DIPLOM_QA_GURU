import allure
import pytest
import faker


@pytest.fixture
@allure.title("Генерация данных для payload с помощью библиотеки Faker")
def generate_payload():
    fake = faker.Faker()
    payload = {
        "id": fake.random_int(2, 10),
        "category": {
            "id": fake.random_int(2, 10),
            "name": fake.name()[0:6]
        },
        "name": fake.name()[0:6],
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": fake.name()[0:6]
            }
        ],
        "status": ""
    }
    return payload
