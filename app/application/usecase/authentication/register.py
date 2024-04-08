"""

Слой Domain:
- entity (сущности, модели), repository interfaces, errors (виды ошибок для конкретной сущности)

Слой Application:
- use case (отдельные микросервисы, например, crud), protocols (интерфейсы), contracts (шаблоны DTO, например BaseModel (Pydantic), dataclass)

Слой Infrastructure:
- IoC (реализация для Dependency Injection), реализация всех репозиториев и т.д

Слой Framework:
- пользовательские интерфейсы взаимодействия с веб-сервером, например, endpoints.


"""