from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from tgFunctions import *

#colocar o numero do telefone com DDD ex: 021 7777-7777
phone = input('Phone number with DDD: ')

browser = webdriver.Firefox()
browser.get('https://web.telegram.org/#/login')
login_telegram(browser, phone)

print('sleep time wait 20 seconds')
sleep(20)
print('sleep time over')

new_tab(browser)
browser.get('https://www.google.com.br/')

new_tab(browser)
browser.get('https://web.telegram.org/#/im?tgaddr=tg%3A%2F%2Fjoin%3Finvite%3DAAAAAEDrakjDNoJR0vtulw')
box = WebDriverWait(browser, 10).until(lambda browser: browser.find_elements_by_tag_name('button'))
print(box)
box.click()

#browser.get('https://web.telegram.org/#/im?tgaddr=tg%3A%2F%2Fjoin%3Finvite%3DAAAAAEDrakjDNoJR0vtulw')
#browser.get('https://t.me/joinchat/AAAAAEDrakjDNoJR0vtulw')
#print(browser)
#links @grupos_ti

#browser.quit()