# Проект: Бронирование номеров
___

Данный проект представляет собой реализацию backend-части
пет-проекта "Бронирование номеров". Данный подпроект реализует
REST API архитектуру с использованием подхода Domain Driven Design и популярными
паттернами разработки (TransactionManager, Repository, Factory, IoC, Dependency Inject. и другие).
Это обеспечивает высокую гибкость, масштабируемость и тестируемость приложения.

### Технологический стек:
___

- Язык программирования: Python 3.11
- База данных: PostgreSQL
- Контейнеризация: Docker
- Веб-фреймворк: FastAPI
- Драйвер для PostgreSQL: Psycopg2 + Asyncpg
- Фреймворк для внедрения зависимостей: Dishka

### Запуск проекта локально без использования контейнеризации
___
1. Клонировать репозиторий: ```git clone https://github.com/iNTENSY/fastapi-ddd-hotels.git```
2. Создать виртуальное окружение ```python -m venv .venv```
3. Активировать виртуальное окружение: (_Windows_) ```.\.venv\Scripts\activate```
или (_Linux_) ```source ./.venv/bin/activate``` 
4. Установить имеющиеся библиотеки: ```pip install -r requirements.txt```
5. Создать файл с переменными окружения из ```.env.example```.
Файл назвать ```.env```
6. Проверить и применить миграции с помощью alembic: 
```
alembic revision --autogenerate
alembic update head
```
