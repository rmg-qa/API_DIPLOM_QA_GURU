import random
import allure
import pytest
import faker

status = ["available", "pending", "sold"]


@pytest.fixture
@allure.title("Генерация данных с помощью библиотеки Faker")
def _payload():
    fake = faker.Faker()
    payload = {
        "id": fake.random_int(1, 5),
        "category": {
            "id": fake.random_int(1, 5),
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
        "status": random.choice(status)
    }
    return payload
