# Final_SkyPro  

## Шаблон для автоматизации тестирования на python

### Стек:
- pytest
- selenium
- requests
- _sqlalchemy_
- allure

### Шаги
1. Склонировать проект 'git clone https://github.com/Yulchona2/Final_SkyPro.git'
2. Установить зависимости 'pip install -r requirements.txt'
3. Подставить в файле data.py в папке data свой токен авторизации в HEADERS_PROJECT
4. Запустить тесты 'pytest'
5. Некоторые UI тесты падают при прогоне всех тестов сразу - запустить по одному.
6. В некоторых тестах меняется порядок появления всплывающих окон для принятия cookie и
предложения войти или зарегистрироваться.

### Структура
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)


