# Дипломный проект. Выполнение API-автотестов бесплатного сервиса "Petstore" 
> [Petstore](https://petstore.swagger.io/#/ )
> 
![Screenshoot](/images/petstore.png)

### Список реализованных API-тестов:

* ✅ Параметризация на получение питомцев со всеми статусами
* ✅ GET-запрос на получение определенного питомца по его id
* ✅ Создаем питомца и проверяем, что питомец создался корректно
* ✅ Создаем питомца и меняем его имя
* ✅ Проверка удаления питомца

### Используемые технологии
<p  align="center">
   <code><img width="5%" title="Python" src="images/python.png"></code>
   <code><img width="5%" title="PyCharm" src="images/pycharm.png"></code>
   <code><img width="5%" title="Pytest" src="images/pytest.png"></code>
   <code><img width="5%" title="Requests" src="images/requests.png"></code>
   <code><img width="5%" title="Jsonschema" src="images/jsonschema.png"></code>
   <code><img width="5%" title="Jenkins" src="images/jenkins.png"></code>
   <code><img width="5%" title="Allure Report" src="images/allure_report.png"></code>
   <code><img width="5%" title="Allure TestOps" src="images/allure_testops.png"></code>
   <code><img width="5%" title="Jira" src="images/jira.png"></code>
   <code><img width="5%" title="Telegram" src="images/tg.png"></code>
</p>

* `Python v. 3.13`: язык программирования; 
* `Pycharm`: среда разработки (IDE) для языка программирования Python;   
* `PyTest`: библиотека модульного тестирования. В автотестах реализована параметризация;  
* `Requests`: библиотека для работы с HTTP-запросами в Python;  
* `Jsonschema`: библиотека, которая позволяет определить ожидаемую структуру JSON-объекта;  
* `Jenkins`: инструмент CI/CD - с помощью этого инструмента реализован удаленный запуск автотестов, отправка уведомлений в Telegram, интеграция с TMS;  
* `ТестОпс`: TMS-платформа для управления тестированием программного обеспечения. Реализована интеграция с Jira;  
* `Jira`: комплексная система управления проектами;  
* `Allure Report`: собирает графический отчет о прохождении автотестов;  
* `BotFather`: настраиваемый бот в Telegram - с его помощью результаты прогона автотестов присылаются в Telegram в виде небольшого мини-отчета. 

### Локальный запуск API-тестов

1. Скачать проект и открыть в Pycharm   

2. Создайте и активируйте виртуальное окружение
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Установите зависимости с помощью pip
   ```bash
   pip install -r requirements.txt
   ```
4. Для запуска автотестов выполните команду:<br>
    ```bash
      pytest tests
    ```

5. Выполнить запрос на формирование allure-отчета:
    ```bash
    allure serve allure-results
    ```

<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="images/jenkins.png"> Запуск проекта в Jenkins
### [Задача в Jenkins](https://jenkins.autotests.cloud/job/API_DIPLOM_ROMAN_GOROKHOVIK/)
![This is a image](images/api_job.png)


<!-- Allure report -->

### <img width="3%" title="Allure Report" src="images/allure_report.png"> Allure report

##### Результаты выполнения тестов можно посмотреть в Allure-отчете
![This is a image](images/allure_title.png)


<!-- Allure TestOps -->

### <img width="3%" title="Allure TestOps" src="images/allure_testops.png"> Интеграция с Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/5023/dashboards)

![This is an image](images/dash_api.png)
![This is an image](images/suites_api.png)



<!-- Jira -->

### <img width="3%" title="Jira" src="images/jira.png"> Интеграция с Jira

![This is an image](images/jira_1.png)
![This is an image](images/jira_2.png)


<!-- Telegram -->

### <img width="3%" title="Telegram" src="images/tg.png"> Оповещения в Telegram
##### После выполнения тестов в Telegram bot приходит сообщение с графиком и информацией о тестовом прогоне.

![Notifications tg](images/notification_tg.png)