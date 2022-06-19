# -ImportGSheetsAPI

-------------------------------------------------------------------------------------------------------------

Для функционирования выгрузки из GoogleSheetsAPI необходимо:
1. Создать личный проект на https://console.cloud.google.com/.
![Screenshot](./doc/img/docScreenshot.png)
2. Подключить для него 2 API: Google Drive API и Google Sheets API
3. Создать учетные данные для Google Drive API с ролью Проект-Редактор. 
4. Выгрузить json аккаунта.
4. Полученный файл поместить в папку ./backend/g_sheets/ и переименовать в creds.json
5. Сгенерированный при создании учетной записи email добавить в пользователи отслеживаемой таблицы.

-------------------------------------------------------------------------------------------------------------

Текущий проект расчитан на получение максимум 5000 записей. В случае превышения данного лимита, необходимо в файле run.py изменить диапазон в переменной "range" (пример: "A1:D10000")

-------------------------------------------------------------------------------------------------------------