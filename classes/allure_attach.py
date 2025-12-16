import json
from allure_commons.types import AttachmentType

import allure


class AllureLoggingMethods:

    @staticmethod
    def logging_request_json(request_body, name):
        allure.attach(
            body=json.dumps(request_body, indent=4, ensure_ascii=True),
            name=name,
            attachment_type=allure.attachment_type.JSON
        )

    @staticmethod
    def logging_response_json(result, name):
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True),
                      name=name,
                      attachment_type=AttachmentType.JSON,
                      extension="json")


class AllurePetLoggingMethods:

    @staticmethod
    def logging_delete_pet(id_pet, result, name):
        # Логируем id питомца
        allure.attach(
            body=str(id_pet) or "",
            name='id питомца',
            attachment_type=allure.attachment_type.TEXT
        )

        allure.attach(
            body=json.dumps(result.json(), indent=4, ensure_ascii=True),
            name=name,
            attachment_type=AttachmentType.JSON,
            extension="json"
        )
