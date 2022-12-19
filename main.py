"""
скрипт для выставления на продажу лотов Теле2.
Пока по 2 Гб как самые популярные
"""
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from account import login, passw
from fake_useragent import UserAgent
from selenium.webdriver.firefox.options import Options
from PyQt6.QtWidgets import QApplication, QWidget


# app = QApplication([])
# window = QWidget()
# window.show()
#
#
# app.exec()


ua = UserAgent().random
options = Options()
options.add_argument(f'--user-agent={ua}')
driver = webdriver.Firefox(options=options)


def wait(selector):
    WebDriverWait(driver, 10, 0.3).until(ec.presence_of_element_located((By.CSS_SELECTOR, selector)))


def click(selector):
    driver.find_element(By.CSS_SELECTOR, selector).click()


def send_keys(selector, keys):
    driver.find_element(By.CSS_SELECTOR, selector).send_keys(keys)


def smile():  # добавить 3 смайлика кота :) :) :)
    cat = '.emoji-field__available-values-block > img:nth-child(2)'
    wait(cat)
    for i in range(4):
        click(cat)


try:
    driver.get('https://tele2.ru/')
    enter_button = '.login-action-short-text'
    wait(enter_button)
    click(enter_button)
    enter_with_passw = 'button.unstyled-button:nth-child(2)'
    wait(enter_with_passw)
    click(enter_with_passw)
    login_field = '[name=username]'
    passw_field = '[name=password]'
    wait(login_field)
    send_keys(login_field, login)
    send_keys(passw_field, passw)
    click('[type=submit]')

    driver.get('https://tele2.ru/stock-exchange/my')
    make_lot_button = 'a.btn.btn-black.hidden-xs'
    wait(make_lot_button)
    click(make_lot_button)
    next_button = 'div.btns-box a.btn.btn-black'
    wait(next_button)
    click(next_button)
    enter_GB = '.lot-setup-popup > div:nth-child(2) > a:nth-child(1)'
    wait(enter_GB)
    click(enter_GB)
    number_of_GB = '[name=lotVolume]'
    driver.find_element(By.CSS_SELECTOR, number_of_GB).send_keys(Keys.BACKSPACE)
    send_keys(number_of_GB, '2')
    click('div.lot-setup__manual-input a')
    GB_price = '[name=lotCost]'
    driver.find_element(By.CSS_SELECTOR, GB_price).send_keys(Keys.BACKSPACE, Keys.BACKSPACE)
    send_keys(GB_price, '30')
    click('div.btns-box a.btn.btn-black')
    smile()
    click('.btns-box > a:nth-child(1)')

finally:
    driver.quit()
