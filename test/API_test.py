import requests

headers_project = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIyMzQ5NjIyLCJpYXQiOjE3NTc5NjkwMDQsImV4cCI6MTc1Nzk3MjYwNCwidHlwZSI6MjAsImp0aSI6IjAxOTk0ZjFlLTM2MmQtN2ZlZi04Yzk1LWE5ZjlhODFiNWVhMSIsInJvbGVzIjoxMH0.SNrED0nl2rwKYbdIIMdjW7RE5vOZqqzdqd3eonbWhV4",
         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
    }
base_url_API = "https://web-gate.chitai-gorod.ru/api/v2"
base_url_search = base_url_API + "/search/product"
params_full_name = {
    "customerCityId": 213,
    "sortPreset": "relevance",
    "products[page]": 1,
    "products[per-page]": 60,
    "phrase": "Волшебник Изумрудного города"
}
params_one_word = {
    "customerCityId": 213,
    "sortPreset": "relevance",
    "products[page]": 1,
    "products[per-page]": 60,
    "phrase": "Волшебник Изумрудного города"
}
params_two_letters = {
    "customerCityId": 213,
    "sortPreset": "relevance",
    "products[page]": 1,
    "products[per-page]": 60,
    "phrase": "Во"
}
params_one_letter = {
    "customerCityId": 213,
    "sortPreset": "relevance",
    "products[page]": 1,
    "products[per-page]": 60,
    "phrase": "В"
}
params_empty = {
    "customerCityId": 213,
    "sortPreset": "relevance",
    "products[page]": 1,
    "products[per-page]": 60,
    "phrase": ""
}


# Поиск книг по полному названию
def test_search_books_full_title():
    response = requests.get(base_url_search, params=params_full_name, headers=headers_project)
    data = response.json()
    assert response.status_code == 200
    assert data["included"][0]["attributes"]["title"] == "Волшебник Изумрудного города"


# Поиск книг по одному слову
def test_search_books_one_word():
    response = requests.get(base_url_search, params=params_one_word, headers=headers_project)
    data = response.json()
    assert response.status_code == 200
    assert len(data) > 0


# Поиск книги по двум символам
def test_search_books_two_letters():
    response = requests.get(base_url_search, params=params_two_letters, headers=headers_project)
    data = response.json()
    assert response.status_code == 200
    assert len(data) > 0


# Поиск книги по одному символу
def test_search_books_one_letter():
    response = requests.get(base_url_search, params=params_one_letter, headers=headers_project)
    data = response.json()
    assert response.status_code == 400
    assert data["errors"][0]["title"] == "Phrase должен содержать минимум 2 символа"


# нулевой поиск
def test_search_books_empty():
    response = requests.get(base_url_search, params=params_empty, headers=headers_project)
    data = response.json()
    assert response.status_code == 400
    assert data["errors"][0]["title"] == "Phrase обязательное поле"
