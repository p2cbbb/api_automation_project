# Проект по автоматизации API с использованием Python и Pytest

### Задание:
> Написать проект для автоматизированного тестирования API и HTTP-методов: POST, GET, PUT, DELETE.

### Копирование репозитория и установка зависимостей
```bash
git clone https://github.com/p2cbbb/api_automation_project
cd api_automation_project
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Запуск тестов
 - Перед запуском тестов необходимо перейти в каталог проекта `https://github.com/p2cbbb/api_automation_project`
 
Аргументы запуска:
- -s - показывать принты в процессе выполнения
- -v - verbose режим, чтобы видеть, какие тесты были запущены
```bash
python -m pytest -v -s tests
```