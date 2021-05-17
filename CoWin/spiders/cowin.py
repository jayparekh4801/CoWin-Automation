import scrapy
from selenium import webdriver
import time


class CowinSpider(scrapy.Spider):
    name = 'cowin'
    allowed_domains = ['https://selfregistration.cowin.gov.in/']
    # start_urls = ['https://selfregistration.cowin.gov.in/']

    def start_requests(self):
        self.wb = webdriver.Chrome()
        self.wb.get('https://selfregistration.cowin.gov.in/')
        inputOTP = self.wb.find_element_by_xpath('//input[@type="number"]')
        inputOTP.click()
        inputOTP.send_keys(9328625398)
        otpButton = self.wb.find_element_by_xpath('//ion-button[@type = "button"]')
        otpButton.click()
        time.sleep(2)
        otpField = self.wb.find_element_by_xpath('//input[@formcontrolname = "otp"]')
        while True :
            time.sleep(7)
            if(len(otpField.get_attribute('value')) == 6) :
                # print("hiiiiiiiiiiihihihhihihihihihiiiiihihi")
                otp2button = self.wb.find_element_by_xpath('//ion-button[@type = "button"]')
                otp2button.click()
                # break
        # time.sleep(2)
        # scheduleButton = self.wb.find_element_by_xpath('//div[@class = "covid-button-desktop book-btn ng-star-inserted"]')
        # scheduleButton.click()
        # otpField.click()
        # otpField.send_keys(999999)

    def parse(self, response):
        pass
