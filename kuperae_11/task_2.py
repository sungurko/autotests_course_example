# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from time import sleep
import os

mes = 'Ты скажи ему привет, скажет он "привет" в ответ'

site = 'https://fix-online.sbis.ru/'
driver = webdriver.Chrome()
# Вынес сюда локаторы, слишком длинные
locators = {'login_user': '[name = "Login"]',
            'password_user': '[name="Password"]',
            'page': '[class="controls-Button__icon controls-BaseButton__icon controls-icon_size-m '
                    'controls-icon_style-contrast controls-icon icon-SabyBird"]',
            'message': '[class="ws-ellipsis controls-Menu__content-wrapper_width"]',
            'select_button': '[class="controls-Button__icon controls-BaseButton__icon controls-icon_size-s '
                             'controls-icon_style-contrast controls-icon icon-Yes"]',
            'input_field': '.controls-Field',
            'button': '[class="controls-Button__icon controls-BaseButton__icon controls-icon_size-s '
                      'controls-icon_style-contrast controls-icon icon-Yes"]',
            'text_editor': '[class="textEditor_Viewer__Paragraph"]',
            'recipient': '.addressee-selector-popup__view-item-wrapper',
            'button_send': '[class="controls-Button__icon controls-BaseButton__icon controls-icon_size-s '
                           'controls-icon_style-contrast controls-icon icon-BtArrow"]',
            'contacts': '[data-qa="counter"]',
            'new_message': '.msg-entity-text',
            'del': '[class="ws-ellipsis controls-Menu__content-wrapper_width"]'}

try:
    driver.get(site)
    sleep(4)
    login = driver.find_element(By.CSS_SELECTOR, locators['login_user'])
    login.send_keys('klient_sergeev', Keys.ENTER)
    sleep(6)
    password = driver.find_element(By.CSS_SELECTOR, locators['password_user'])
    password.send_keys(os.environ['fix_pass'], Keys.ENTER)
    sleep(7)
    main_page = driver.find_element(By.CSS_SELECTOR, locators['page'])
    sleep(7)
    main_page.click()
    sleep(7)
    message = driver.find_elements(By.CSS_SELECTOR, locators['message'])[-2]
    sleep(5)
    message.click()
    sleep(5)
    text = driver.find_elements(By.CSS_SELECTOR, locators['input_field'])[0]
    text.send_keys('Сергеев Сергей', Keys.ENTER)
    sleep(5)
    recipient = driver.find_element(By.CSS_SELECTOR, locators['recipient'])
    recipient.click()
    sleep(5)
    text_editor = driver.find_element(By.CSS_SELECTOR, locators['text_editor'])
    sleep(7)
    text_editor.send_keys('Ты скажи ему привет, скажет он "привет" в ответ', Keys.ENTER)
    sleep(5)
    send = driver.find_element(By.CSS_SELECTOR, locators['button_send'])
    send.click()
    sleep(5)
    contacts = driver.find_elements(By.CSS_SELECTOR, locators['contacts'])[0]
    contacts.click()
    sleep(5)
    new_message = driver.find_elements(By.CSS_SELECTOR, locators['new_message'])[0]
    assert new_message.text == mes
    action_chains = ActionChains(driver)
    action_chains.move_to_element(new_message)
    action_chains.context_click(new_message)
    action_chains.perform()
    delete = driver.find_elements(By.CSS_SELECTOR, locators['del'])[-1]
    sleep(5)
    delete.click()
    sleep(10)
    del_messages = driver.find_element(By.CSS_SELECTOR, locators['new_message'])
    sleep(5)
    assert del_messages.text != mes
finally:
    driver.quit()
