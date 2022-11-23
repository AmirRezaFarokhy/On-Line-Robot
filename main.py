from selenium import webdriver
from selenium.webdriver import ActionChains
import time 
from bs4 import BeautifulSoup
from pytz import timezone
from datetime import datetime 

from requests import OnLineRobot

path_Chrome = "chromedriver.exe"

USER_NAME = input("Inter your user name: ") # Inter your user name
PASSWORD = input("Inter your password: ") # Inter your password
LINK_IRAN_MARKET = "https://account.emofid.com/Login"
Iran_tehran = timezone("Asia/Tehran") 
timeInIran = datetime.now(Iran_tehran)
currentTimeInNewYork = timeInIran.strftime("%H:%M:%S")
X = 155 # screen windth (Different for everyone)
y = 335 # screen height (Different for everyone)
END_TIME = "8:46:59"

robots_req = OnLineRobot(USER_NAME, PASSWORD, LINK_IRAN_MARKET)

def main():
	done = False
	while not done:
		robots_req.Robot()
		time.sleep(2)
		start = True
		while start:
			start = robots_req.Send_Click_Requests(X, Y)

		if currentTimeInNewYork==END_TIME:
			done = True

if __name__ == "__main__":
	main()
	
