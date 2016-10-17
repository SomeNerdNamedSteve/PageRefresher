#library imports
from selenium import webdriver
import time
import sys

#url input
x=raw_input("Enter the URL")

#input of and setting refresh rate of web page
refreshrate=raw_input("Enter the number of seconds")
refreshrate=int(refreshrate)

#set web browser to Firefox and get the source fo the driver
driver = webdriver.Firefox()
driver.get("http://"+x)

#infinitely refresh page after refreshrate (in seconds)
while True:
	time.sleep(refreshrate)
	driver.refresh()
