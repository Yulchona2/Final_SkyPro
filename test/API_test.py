import requests

base_url_search_full_name = "https://web-gate.chitai-gorod.ru/api/v2/search/product?"\
                            "customerCityId=213&sortPreset=relevance&products%5Bpage%5D=1&products%5Bper-page%"\
                            "5D=60&phrase=%D0%B2%D0%BE%D0%BB%D1%88%D0%B5%D0%B1%D0%BD%D0%B8%D0%BA%20%D0%B8%D0%B7%"\
                            "D1%83%D0%BC%D1%80%D1%83%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%B0"

headers_project = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIyMzQ5NjIyLCJpYXQiOjE3NTc5MTQ1MzMsImV4cCI6MTc1NzkxODEzMywidHlwZSI6MjAsImp0aSI6IjAxOTk0YmRmLTBlZjQtNzE0My1iY2I0LWE4YzllODQzZDRmZSIsInJvbGVzIjoxMH0.BvDzV6pzPHyHLLmuhZ_Kwy2Zf9jTYSbP-W_bCh2q5L4",
         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
    }
def test_search_books():
    response = requests.get(base_url_search_full_name,  headers=headers_project)
    assert response.status_code == 200
    assert response.json()["data"]["included"][0]["attributes"]["title"] == "Волшебник Изумрудного города"