from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


firefox_options = Options()
firefox_options.headless = False

driver = webdriver.Firefox(executable_path="./geckodriver.exe", options=firefox_options)
driver.maximize_window()
# test 1: Перевірка наявності лого на головній сторінці
driver.get("https://rozetka.com.ua/")
logo = driver.find_element(By.ID, "logo")
assert logo.is_displayed()


# test 2: Пошук товару
driver.get("https://rozetka.com.ua/")
search_input = driver.find_element(By.ID, "search_input")
search_input.send_keys("Marshall Major")
search_input.send_keys(Keys.RETURN)
assert "Marshall Major" in driver.title


# test 3: Вибір категорії товару
driver.get("https://rozetka.com.ua/")
category = driver.find_element(By.ID, "category_link")
category.click()
assert "Побутова техніка" in driver.title


# test 4: Додавання товару до кошика
driver.get("https://rozetka.com.ua/ua/marshall-major-iv-bluetooth-black/p326981896/")
add_to_cart_button = driver.find_element(By.ID, "buy_button")
add_to_cart_button.click()
assert "Корзина" in driver.title


# test 5: Перевірка наявності навігаційного меню з категоріями
driver.get("https://rozetka.com.ua/")
categories_menu = driver.find_element(By.ID, "menu_categories")
assert categories_menu.is_displayed()


driver.close()
