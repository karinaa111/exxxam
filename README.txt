DJANGO API: /branches

ВСТАНОВЛЕННЯ:
  python -m venv venv
  # Windows:
  venv\Scripts\activate
  # Linux/Mac:
  source venv/bin/activate
  pip install -r requirements.txt

ЗАПУСК:
  python manage.py migrate
  python manage.py seed          # додає 3 тестові філії
  python manage.py runserver

ЕНДПОЙНТИ:
  GET  http://127.0.0.1:8000/branches/        — список усіх філій
  PUT  http://127.0.0.1:8000/branches/<id>/   — оновити філію
       Body (JSON): {"name":"...","address":"...","phone":"..."}

ПРИКЛАДИ:
  curl http://127.0.0.1:8000/branches/
  curl -X PUT http://127.0.0.1:8000/branches/1/ ^
       -H "Content-Type: application/json" ^
       -d "{\"name\":\"Оновлена назва\"}"
