from selenium import webdriver
import time, sys
import selenium
import csv
from datetime import datetime

def scraper(text):
	try:
		a = browser.find_element_by_xpath(text)

	except selenium.common.exceptions.NoSuchElementException:
		return 0

	if (a.text == 'online'):
		return 1

	if (a.text == 'typing...'):
		return 1

	return 0



#program
print ("Starting...")
browser = webdriver.Firefox()

browser.get('http://web.whatsapp.com')

#get name
name = input('Please enter name:')

#click on the desired chat
print ("Loading...")
try:
	a = browser.find_element_by_xpath("//span[@title='{}']".format(name))
	a.click()

except selenium.common.exceptions.NoSuchElementException:
	sys.exit("invalid name, plase try again")

#write to file
myFile = open('log.csv', 'w')

#check if online
try:
	print("Currently logging...")
	while True:
		data = '="{}"'.format(str(datetime.now())), scraper('//span[@class = "emojitext O90ur"]')
		writer = csv.writer(myFile)
		writer.writerow(data)
		time.sleep(1)
except KeyboardInterrupt:
	pass

print ("Done")
myFile.close()