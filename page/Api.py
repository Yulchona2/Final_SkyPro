import requests

url_for_full_name = "https://web-gate.chitai-gorod.ru/api/v2/search/product?customerCityId=213&sortPreset=relevance&products%5Bpage%5D=1&products%5Bper-page%5D=60&phrase=%D0%B2%D0%BE%D0%BB%D1%88%D0%B5%D0%B1%D0%BD%D0%B8%D0%BA%20%D0%B8%D0%B7%D1%83%D0%BC%D1%80%D1%83%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%B0"

headers_for_projects = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIyMzQ5NjIyLCJpYXQiOjE3NTc2Mjc4ODEsImV4cCI6MTc1NzYzMTQ4MSwidHlwZSI6MjAsImp0aSI6IjAxOTkzYWM5LTE4YWYtNzUzYi1iOTUzLWZkYjk4YTQ0NGU5ZiIsInJvbGVzIjoxMH0.ps4k5ecKTN3EwUckXIkpzVhpRTq0LAa_9DovHqH5Lfc",
        "Cookie": "__ddg1_=G97MaUXpIZEEFSqfb0V7; _ym_uid=1744815450764145642; _ym_d=1744815450; _ga=GA1.1.63755683.1744815452; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=99e5947c-cd67-40ca-80f1-21cb59a63cd8; __P__wuid=15f4e12efb72363bd548e9263ec68dd3; stDeIdU=15f4e12efb72363bd548e9263ec68dd3; chg_visitor_id=2863d36d-8cf3-4a72-9013-3d2818d9d10c; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; tmr_lvid=c28ddca42a248c776094f8335cdf5e6c; tmr_lvidTS=1744815456804; adrcid=AVsbmtuqiPEzQWkosChXmAg; analytic_id=1745565440830654; acs_3=%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1745753277025%2C%22sl%22%3A%7B%22224%22%3A1745666877025%2C%221228%22%3A1745666877025%7D%7D; _ymab_param=L-cUSHfpuc5BJdmlnumPBoL8PxYFbWQtXPXrz-Z4aY_ei0SeobrIndo7uIXDsX0C6bYqpuve_wLN2T2pvDzChqs8lx0; __ddg9_=46.39.228.250; vIdUid=1f7b353d-3593-4171-a014-f0f184c80eae; stSeStTi=1745736486296; adrdel=1745736486943; refresh-token=Xe9ukJEe7kXlbEF1ATf6JBaOwM88VWvmbM8X3gGz9IZwFNm8PLeJOUGOxv8f2r9wHhGKa1cdgWM2YXvp; tid-state=504f71d1-88bc-41d5-af08-8bfc032802d2; tid-redirect-uri=https%3A%2F%2Fwww.chitai-gorod.ru%2Fauth%2Ft-id; stLaEvTi=1745737090504; mindboxDeviceUUID=c6ab944b-2d4b-4e7a-afeb-d13a522843ac; directCrm-session=%7B%22deviceGuid%22%3A%22c6ab944b-2d4b-4e7a-afeb-d13a522843ac%22%7D; _ga_W0V3RXZCPY=GS1.1.1745736486.12.1.1745740077.0.0.0; _ga_6JJPBGS8QY=GS1.1.1745736486.12.1.1745740077.0.0.0; access-token=Bearer%20eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIyMzQ5NjIyLCJpYXQiOjE3NDU3NDA4MjEsImV4cCI6MTc0NTc0NDQyMSwidHlwZSI6MjB9.0rLKkadkZt5BDG7h8Zgpg53-7LXABv8TaoVzGKpmgtU; __ddg8_=NHYhecI7MqAA7jee; __ddg10_=1745740827; _ga_LN4Z31QGF4=GS1.1.1745736486.12.1.1745740830.52.1.984976907; tid-back-to=%7B%22fullPath%22%3A%22%2Fsearch%3Fphrase%3D%25D0%25B2%25D0%25BE%25D0%25BB%25D1%2588%25D0%25B5%25D0%25B1%25D0%25BD%25D0%25B8%25D0%25BA%2B%25D0%25B8%25D0%25B7%25D1%2583%25D0%25BC%25D1%2580%25D1%2583%25D0%25B4%25D0%25BD%25D0%25BE%25D0%25B3%25D0%25BE%2B%25D0%25B3%25D0%25BE%25D1%2580%25D0%25BE%25D0%25B4%25D0%25B0%22%2C%22hash%22%3A%22%22%2C%22query%22%3A%7B%22phrase%22%3A%22%D0%B2%D0%BE%D0%BB%D1%88%D0%B5%D0%B1%D0%BD%D0%B8%D0%BA%20%D0%B8%D0%B7%D1%83%D0%BC%D1%80%D1%83%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%B0%22%7D%2C%22name%22%3A%22search%22%2C%22path%22%3A%22%2Fsearch%22%2C%22params%22%3A%7B%7D%2C%22meta%22%3A%7B%22pageTransition%22%3Afalse%7D%7D"
    }


class Api:

    def __init__(self, url):
        self.url = url

    def get_by_full_name():
        resp = requests.get(url_for_full_name, headers=headers_for_projects)
        return resp
