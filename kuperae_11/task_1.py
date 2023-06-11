# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


site = 'https://sbis.ru/'
driver = webdriver.Chrome()
# Вынес сюда локаторы, слишком длинные
locators = ['a.sbisru-Header__menu-link[href="/contacts"]',
            '[class="sbisru-Contacts__logo-tensor mb-8"]',
            '[class="tensor_ru-Index__block4-content tensor_ru-Index__card"]',
            '[class="tensor_ru-link tensor_ru-Index__link"]']

try:
    driver.get(site)
    contact_btn = driver.find_element(By.CSS_SELECTOR, locators[0])
    contact_btn.click()  # Клик по кнопке "Контакты"
    sleep(2)
    banner = driver.find_element(By.CSS_SELECTOR, locators[1])
    banner.click()  # Клик по баннеру Тензор
    driver.switch_to.window(driver.window_handles[1])
    strong_men = driver.find_element(By.CSS_SELECTOR, locators[2])
    sleep(2)
    assert strong_men.text.split('\n')[0] == 'Сила в людях'
    actions = ActionChains(driver)
    actions.move_to_element(strong_men)
    actions.perform()  # Скролл до кнопки "Подробнее"
    sleep(2)
    more = driver.find_elements(By.CSS_SELECTOR, locators[3])[1]  # Нашел 2 элемента, кликнуть по второму
    more.click()  # Клик по "Подробнее"
    assert driver.current_url == 'https://tensor.ru/about'
    sleep(2)
finally:
    driver.quit()
    