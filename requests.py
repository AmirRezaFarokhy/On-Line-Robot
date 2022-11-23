from selenium import webdriver
from selenium.webdriver import ActionChains
import time 
from bs4 import BeautifulSoup
from mouse import move, click 
from pytz import timezone
from datetime import datetime 

path_Chrome = "chromedriver.exe" # for selenium google page

class OnLineRobot:

	def __init__(self, user_name, password_user, usrl):
		self.user_name = user_name
		self.password_user = password_user
		self.link = usrl
		self.start_time = "8:45:59"

	def Robot(self):
		driver = webdriver.Chrome(path_Chrome)
		driver.get(url)
		time.sleep(1)

		element = driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div[1]/div/form/fieldset/div[1]/div[1]/input")
		ActionChains(driver).click(element).perform()
		element.send_keys(USER_NAME)
		time.sleep(4)

		password = driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div[1]/div/form/fieldset/div[2]/div[1]/input")
		ActionChains(driver).click(password).perform()
		password.send_keys(password_user)
		time.sleep(3)

		btn2 = driver.find_element_by_xpath('//*[@id="submit_btn"]')	
		ActionChains(driver).click(btn2).perform()
		time.sleep(2)

		bot = driver.find_element_by_xpath("/html/body/div/div/div/div/div[1]/div/div/a[2]")
		ActionChains(driver).click(bot).perform()
		time.sleep(2)

		easy_trade = driver.find_element_by_xpath("/html/body/nav/div/div/a/span")
		ActionChains(driver).click(easy_trade).perform()


	def Send_Click_Requests(self, x, y):
	    Iran_tehran = timezone("Asia/Tehran") 
	    timeInIran = datetime.now(Iran_tehran)
	    currentTimeInNewYork = timeInIran.strftime("%H:%M:%S")
	    
	    if currentTimeInNewYork==self.start_time:
	        for _ in range(1000000):
	            start = time.time()
	            move(x, y, absolute=True)
	            #click()
	            #time.sleep(0.018)
	            end = time.time()
	            print(end-start)
	            
	        return False

	   	driver.quit()

	    return True


