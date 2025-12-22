# Budget Tracking (Personal Finance Tracker)

Повний стек для обліку особистих фінансів: бекенд на Django + MongoDB, фронтенд на React/Vite. Є API для гаманців, транзакцій і валют, плюс інтерактивна клієнтська частина.

## Технології
- Backend: Django 6, Django REST Framework, MongoDB (django-mongodb-backend), OpenAPI/Swagger через drf-spectacular.
- Frontend: React 19, Vite, React Router.
- Інше: Docker Compose для MongoDB, python-dotenv для змінних середовища.

## Запуск бекенду
1. `cd backend`
2. Створіть віртуальне середовище: `python -m venv .venv && .\.venv\Scripts\activate`
3. Скопіюйте `.env.example` → `.env` і заповніть `MONGODB_URI`, `MONGODB_NAME`, `SECRET_KEY`, `DEBUG`.
4. Підніміть MongoDB: `docker compose up -d`
5. Встановіть залежності: `pip install -r requirements.txt`
6. Застосуйте міграції: `python manage.py migrate`
7. Заповнити довідник валют: `python manage.py seed_currencies`
8. Запуск: `python manage.py runserver 0.0.0.0:8000`
9. Документація: Swagger `http://localhost:8000/api/docs`, ReDoc `http://localhost:8000/api/redoc`.

## Запуск фронтенду
1. `cd frontend`
2. Встановіть залежності: `npm install`
3. Dev-сервер: `npm run dev` (зазвичай на `http://localhost:5173`)
