from page.MainPage import MainPage

test_phone_number = "+7 (916) 458-79-63"
test_name = "Волшебник Изумрудного города"


def test_search(driver):
    main_page = MainPage(driver)
    main_page.confirm_location()
    main_page.enter_or_registrate()
    main_page.confirm_cookie()
    main_page.search_full_name(test_name)
    title = main_page.found_books()
    assert test_name in title


# Проверяем, что до ввода номера телефона кнопка "Получить код" не активна
def test_button_disabled_before_phone_input(driver):
    main_page = MainPage(driver)
    main_page.confirm_location()
    main_page.confirm_cookie()
    main_page.enter_or_registrate()
    main_page.open_authorization_window()
    button = main_page.get_button()
    print("Текст кнопки:", button.text)
    print("Атрибут 'disabled':", button.get_attribute("disabled"))
    print("Атрибут 'class':", button.get_attribute("class"))
    assert not button.is_enabled()


# Проверяем, что номер телефона записался правильно в поле ввода
def test_insert_phone_number(driver):
    main_page = MainPage(driver)
    main_page.confirm_location()
    main_page.enter_or_registrate()
    main_page.confirm_cookie()
    main_page.open_authorization_window()
    phone_number = test_phone_number
    received_phone_number = main_page.insert_phone_number(phone_number)
    assert received_phone_number == phone_number


def test_count_products_after_one_add(driver):
    main_page = MainPage(driver)
    main_page.confirm_location()
    main_page.enter_or_registrate()
    main_page.confirm_cookie()
    main_page.search_full_name(test_name)
    main_page.add_to_cart()
    main_page.go_to_cart()
    count = main_page.get_count_products()
    assert count == 1


def test_clear_cart(driver):
    main_page = MainPage(driver)
    main_page.confirm_location()
    main_page.enter_or_registrate()
    main_page.search_full_name(test_name)
    main_page.add_to_cart()
    main_page.go_to_cart()
    main_page.clear_cart()
    info = main_page.get_information()
    assert "Корзина очищена" in info
