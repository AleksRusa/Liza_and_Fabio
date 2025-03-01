# Liza_and_Fabio

2. Получение данных из Google Forms через Google Sheets
Когда пользователи отправляют ответы в Google Form, они автоматически сохраняются в Google Таблицах. Вы можете использовать Google Sheets API для доступа к этим данным.

Шаги:
Связь Google Forms с Google Sheets:

В Google Forms нажмите на значок Google Таблиц (в разделе "Ответы"), чтобы создать связанный лист.
Настройка доступа через Google Sheets API:

Настройте Google Cloud Console и включите Google Sheets API (см. инструкцию ниже).
Напишите скрипт для чтения данных из таблицы.
Пример использования Google Sheets API для чтения данных с Python:

python
Копировать
Редактировать
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# Укажите путь к вашему JSON-файлу с ключами
SERVICE_ACCOUNT_FILE = 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# Подключение к Google Sheets
credentials = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# ID Google Таблицы (из URL)
SPREADSHEET_ID = 'YOUR_SPREADSHEET_ID'
RANGE_NAME = 'Sheet1!A1:C10'

service = build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()

# Чтение данных
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
rows = result.get('values', [])

print("Полученные данные:")
for row in rows:
    print(row)
