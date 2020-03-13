from selenium import webdriver
from helpers.selenium_api_wrappers import SeleniumAPIWrapper
from common.variables import *

class Browser(SeleniumAPIWrapper):

	def __init__(self):
		
		if browser_type == 'chrome':

			chromeOptions = webdriver.ChromeOptions()
			chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
			chromeOptions.add_argument("--no-sandbox")
			chromeOptions.add_argument("--disable-setuid-sandbox") 
			chromeOptions.add_argument("--remote-debugging-port=9222")
			chromeOptions.add_argument("--disable-dev-shm-using")
			chromeOptions.add_argument("--disable-extensions")
			chromeOptions.add_argument("--disable-gpu")
			chromeOptions.add_argument("start-maximized")
			chromeOptions.add_argument("disable-infobars")
			chromeOptions.add_argument("--headless")

			self.driver = webdriver.Chrome(chrome_options=chromeOptions)
	

		elif browser_type == 'firefox':
			self.driver = webdriver.Firefox()
		
		super().__init__(self.driver) 

		# context.driver = self.driver

	def close_browser(self):
		self.driver.quit()
