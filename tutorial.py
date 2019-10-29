from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


btn_acceptcontinue_id='com.android.chrome:id/terms_accept'
btn_signin_id="com.android.chrome:id/positive_button"
btn_negative_id ="com.android.chrome:id/negative_button"

field_searchbar_id = "com.android.chrome:id/url_bar"
searchinput_id1= "com.android.chrome:id/search_box_text"

##web id
searchinput_id ="fakebox-input";
web_searchinput_css = ".gLFyf";
elonwikipedia_css ="a[href='https://en.m.wikipedia.org/wiki/Elon_Musk']"



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'Nexus_5X_API_25'
desired_caps['appPackage'] = 'com.android.chrome'
desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'
desired_caps['platformVersion'] = '7.1.1'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

wait = WebDriverWait(driver, 20)

element = WebDriverWait(driver, 20).until(
 EC.presence_of_element_located((By.ID, btn_acceptcontinue_id)))

driver.find_element_by_id(btn_acceptcontinue_id).click();

element = WebDriverWait(driver, 20).until(
 EC.presence_of_element_located((By.ID, btn_negative_id)))
driver.find_element_by_id(btn_negative_id).click();


element = WebDriverWait(driver, 20).until(
 EC.presence_of_element_located((By.ID, searchinput_id1)))
driver.find_element_by_id(searchinput_id1).click();
driver.find_element_by_id(field_searchbar_id).send_keys("Elon Musk \n")

webview = driver.contexts[1]
driver.switch_to.context(webview)

element = WebDriverWait(driver, 20).until(
 EC.presence_of_element_located((By.CSS_SELECTOR, web_searchinput_css)))
driver.find_element_by_css_selector(web_searchinput_css).click();
driver.find_element_by_css_selector(web_searchinput_css).clear()
driver.find_element_by_css_selector(web_searchinput_css).send_keys("Elon Musk wikipedia \n")

element = WebDriverWait(driver, 20).until(
 EC.presence_of_element_located((By.CSS_SELECTOR, elonwikipedia_css)))
driver.find_element_by_css_selector(elonwikipedia_css).click();

driver.execute_script("window.scrollBy(0,6000)");