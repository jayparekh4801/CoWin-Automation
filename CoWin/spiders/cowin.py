from selenium import webdriver
import time
wb = webdriver.Chrome()

wb.get("https://selfregistration.cowin.gov.in/")
time.sleep(2)

number_input = wb.find_element_by_xpath('//input[@type="number"]')
number_input.send_keys(9328625398)
time.sleep(2)

wb.find_element_by_xpath('//ion-button[@type = "button"]').click()
time.sleep(15)

wb.find_element_by_xpath('//ion-button[@type = "button"]').click()
time.sleep(10)