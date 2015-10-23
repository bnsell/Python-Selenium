from selenium import webdriver
from selenium.webdriver.common import action_chains, keys
import time

driver = webdriver.Firefox()
driver.get('Your URL here...')
assert 'NBA' in driver.page_source
action = action_chains.ActionChains(driver)

# open up the developer console
action.send_keys(keys.Keys.COMMAND+keys.Keys.ALT+'i')
action.perform()
time.sleep(3)
# this below ENTER is to rid of the above "i"
action.send_keys(keys.Keys.ENTER)
# inject the JavaScript
action.send_keys("document.querySelectorAll('label.boxed')[1].click()"+keys.Keys.ENTER)
action.perform()
