# -ImportGSheetsAPI
Таблица выгрузки заказов из Google Sheets и отображении ее на сайте в режиме реального времени.
-------------------------------------------------------------------------------------------------------------

Для функционирования выгрузки из GoogleSheetsAPI необходимо:
1. Создать личный проект на https://console.cloud.google.com/.

    Открываем панель выбора проекта
    ![Screenshot](./doc/img/CreateProj.png)

    Переходим в создание нового проекта
    ![Screenshot](./doc/img/CreateProj2.png)

    Присвойте ему произвольное имя и нажмите кнопку Create
    ![Screenshot](./doc/img/CreateProj3.png)

    Для выбор проекта, выберите созданный проект из списка проектов и нажмите на кнопку Open. Данный проект
    будет выбран и его название также будет отображаться на главной странице Google Cloud Platform
    ![Screenshot](./doc/img/CreateProj3.png)
    

2. Подключить для него 2 API: Google Drive API и Google Sheets API

    В навигационном меню выбираем "APIs & Services" -> "Enabled APIs & Services"
    ![Screenshot](./doc/img/AddAPI.png)

    В поиске вводим название необходимого API. В выпадающем списке выбираем соответствующее API из группы "Marketplace".
    ![Screenshot](./doc/img/AddAPI2.png)

    Нажимаем кнопку Enable.
    ![Screenshot](./doc/img/AddAPI3.png)

    Повторяем аналогичные действия для второго из перечисленных API.

3. Создать учетные данные для Google Drive API с ролью Проект-Редактор. 

    В навигационном меню выбираем "APIs & Services" -> "Enabled APIs & Services"
    ![Screenshot](./doc/img/AddAPI.png)

    В нижней части окна, в списке API проекта, выбираем ранее добавленный Google Drive API
    ![Screenshot](./doc/img/CreateCredentials.png)

    Выбираем "CREATE CREDENTIALS"
    ![Screenshot](./doc/img/CreateCredentials2.png)

    Выбираем:
     - "Select an API" ---> "Google Drive API";
     - "What data will you be accessing?" ---> "Application data";
     - "Are you planning to use this API with Compute Engine, Kubernetes Engine, 
     App Engine, or Cloud Functions?" ---> "No, i'm not using them";

     Нажимаем на кнопку "Next"
     ![Screenshot](./doc/img/CreateCredentials3.png)
     ![Screenshot](./doc/img/CreateCredentials4.png)

    Заполняем: 
    - "Service account name" ---> "account"
    Нажимаем "Create and continue"
    ![Screenshot](./doc/img/CreateCredentials5.png)

    Выбираем:
        Role: Project --> Editor
    Нажимаем "Continue"
    Нажимаем "Done"
    ![Screenshot](./doc/img/CreateCredential6.png)


4. Создать и выгрузить json-ключ аккаунта.

    В навигационном меню выбираем "APIs & Services" -> "Credentials"
    ![Screenshot](./doc/img/ImportKey.png)

    В панели "Service Accounts" выбираем наш аккунт.
    ![Screenshot](./doc/img/ImportKey2.png)

    Во вкладке "Keys", выбираем "Add key" --> "Create new key"
    ![Screenshot](./doc/img/ImportKey3.png)

    В появившемся окне выбираем "Json" и нажимаем кнопку "Create"
    ![Screenshot](./doc/img/ImportKey4.png)

    Ключ сформируется,а так же произойдет скачивание файла с ключом на Ваш ПК.

4. Полученный файл поместить в папку ./backend/g_sheets/ данного проекта и переименовать в creds.json. (Внимание!!! ДАнный ключ содержит конфиденциальные данные, ни в коем случае не передавайте их сторонним лицам.)

5. Сгенерированный при создании учетных данных email добавить в пользователи отслеживаемой таблицы.

-------------------------------------------------------------------------------------------------------------
Используемая при создании таблица:
https://docs.google.com/spreadsheets/d/1AZ44qofs3jX3WjIRVVQq9uAwZVd7N6voFKnq-6aNbSU/edit#gid=0

Для создания своей таблицы рекоммендуется:
 - создать таблицу;
 - скопировать данные;
 - добавить сформированный в предыдущих пунктах аккаунт в редакторы таблицы;
 - В файле проекта ./backend/g_sheets/run.py изменнить значение переменной sheet_id, добавив аналогичный фрагмент адреса своей таблицы:
![Screenshot](./doc/img/TableID.png)
-------------------------------------------------------------------------------------------------------------
Текущий проект расчитан на получение максимум 5000 записей. В случае превышения данного лимита, необходимо в файле ./backend/g_sheets/run.py изменить диапазон в переменной "range" (пример: "A1:D10000")

-------------------------------------------------------------------------------------------------------------