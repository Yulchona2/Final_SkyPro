from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
import allure
from time import sleep

base_url = "https://www.chitai-gorod.ru/"


class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def confirm_location(self):
        # Ждем появления плашки "Ваш город - Москва?"
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(
                 (By.CSS_SELECTOR, 'div.header-location-popup')))

        # Ждем кликабельности кнопки "Да, я здесь"и нажимаем на нее
        confirm_button = WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Да, я здесь")]')))
        confirm_button.click()

    def confirm_cookie(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class, 'chg-app-button__content') "
                           "and text()=' Понятно, закрыть ']"))).click()

    def enter_or_registrate(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.popmechanic-main")))
        self.driver.find_element(
            By.CSS_SELECTOR, 'div.popmechanic-close').click()

    @allure.step("Поиск книги по полному названию")
    def search_full_name(self, book_name):
        # Находим поисковую строку
        search_string = self.driver.find_element(
            By.CSS_SELECTOR, 'input[type="search"], input[placeholder*="поиск"], input.search-form__input')
        # Вводим название книги
        search_string.send_keys(book_name)
        search_string.send_keys(Keys.ENTER)

        # Кликаем на кнопку поиска (лупа)
        # self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Найти"]').click()
        self.driver.implicitly_wait(3)

    def found_books(self):
        books = self.driver.find_elements(By.CSS_SELECTOR, "div.app-catalog__content")
        if books:
            title = books[0].find_element(By.CSS_SELECTOR, "a.product-card__title").text
            return title
        return None  # Если книг нет

    def open_authorization_window(self):
        # Ждем кликабельности кнопки "Войти"
        authorize = WebDriverWait(self.driver, 10).until(
              EC.element_to_be_clickable(
                  (By.CSS_SELECTOR, 'span[class="header-controls__text"]')))
        self.driver.implicitly_wait(5)
        authorize.click()
        # Ждем появления формы авторизации
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'tid-form')))

    # Проверка возможности ввода номера телефона
    def insert_phone_number(self, phone_number):
        # Ждем кликабельности поля ввода номера телефона
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "tid-input")))
        phone_input = self.driver.find_element(By.ID, "tid-input")
        phone_input.clear()
        phone_input.send_keys(phone_number)
        return phone_input.get_attribute("value")

    def get_button(self):
        # Находим кнопку "Получить код"
        button = self.driver.find_element(By.CSS_SELECTOR, 'button.chg-app-button[disabled]')
        return button

    # Добавление книги в корзину
    def add_to_cart(self):
        # Ожидаем появления кнопки
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "button.product-buttons__main-action[aria-label='false']")))
        self.driver.implicitly_wait(10)
        sleep(10)
        buy_buttons = self.driver.find_element(
            By.CSS_SELECTOR, "button.product-buttons__main-action[aria-label='false']")

        buy_buttons[0].click()

    # Переход на страницу "Корзина"
    def go_to_cart(self):
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Корзина"]').click()

    # Получить количество товаров в корзине
    def get_count_products(self):
        # Ждем появления элемента с текстом
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span.cart-page__title--append")))

        # Получаем весь текст из элемента
        total_text = element.text  # "1 товар"

        # Извлекаем первую цифру из текста
        count = total_text.split()[0]  # Берем первое слово и преобразуем в число
        return int(count)

    # Очистить корзину
    def clear_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, ".cart-page__clear-cart-title").click()

    # Получить информацию, что корзина очищена
    def get_information(self):
        info = self.driver.find_element(
            By.CSS_SELECTOR, "section.cart-multiple-delete").text
        return info
