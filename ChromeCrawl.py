import re
import mechanize
from selenium import webdriver
import time
import csv
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait

class GetScores(object):

	def getAllScores(self):
		fob=open('c:/Users/Ben/Desktop/Desktop2/CSVs/b.csv','w')
		#browser = webdriver.Firefox()
		browser = webdriver.PhantomJS('c:/PhantomJS/bin/phantomjs.exe')
		
		#Create variable for our XPaths.
		dayNavXPath = "//div[@id='DayNav']/a[1]"
		seasonNavXPath = "//*[@id='DropList']/option[2]"
		scoreboardXPath = "//div[@id='Scoreboard_7']"
		currentDayXPath = "//*[@id='DayNav']/a[2]"
		currentSeasonXPath = "//*[@id='DropList']/option[1]"
		currentYearXPath = "//*[@id='cal']/table/tbody/tr[1]"
		
		def check_xpath_exists(xpath):
			try:
				browser.find_element_by_xpath(xpath)
			except NoSuchElementException:
				return False
			return True
			
		#Get to our website & wait...
		browser.get('http://example.com')
		print "Selenium bot has connected to website..."
		time.sleep(10)
		
		#Grab today's scores
		scores = browser.find_element_by_xpath(scoreboardXPath).text
		print scores	
		
		#Navigate to Previous Day & Wait
		previousDayElement = WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_xpath(dayNavXPath))
		previousDayElement.click()
		print "\nNavigating to previous day...\n"
		time.sleep(4)
		
		#START MAIN LOOP
		i=0
		j=2
		while (i<2):
			#Grab scores and print them.
			scores = browser.find_element_by_xpath(scoreboardXPath).text
			date = "\n"+browser.find_element_by_xpath(currentDayXPath).text
			year = browser.find_element_by_xpath(currentYearXPath).text
			year = year[-8:-3] + "\n"
			finalform = date+year+scores
			fob.write(finalform)
			print date+year
			
			previousDayElement = WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_xpath(dayNavXPath))
			previousDayElement.click()
			print "Navigating to previous day..."
			time.sleep(4)
			
			i+=1
			
			#ARE WE AT BEGINNING OF SEASON? GO TO PREVIOUS SEASON
			if(check_xpath_exists('//*[@id="DayNav"]/a[1]/b')):
				#grab, print scores
				scores = browser.find_element_by_xpath(scoreboardXPath).text
				date = "\n"+browser.find_element_by_xpath(currentDayXPath).text
				year = browser.find_element_by_xpath(currentYearXPath).text
				year = year[-8:-3] + "\n"
				finalform = date+year+scores
				fob.write(finalform)
				print date+year
				
				#Change season
				previousSeasonElement = WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_xpath("//*[@id='DropList']/option["+str(j)+"]"))
				previousSeasonElement.click()
				print "\nclicked previous season...loading\n"
				time.sleep(10)
				
				if(j>9):
					i=9999
				
				j+=1
		
		#END MAIN LOOP
		
		#CHANGE SEASON
		previousSeasonElement = WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_xpath(seasonNavXPath))
		previousSeasonElement.click()
		print "\nclicked previous season...loading\n"
		time.sleep(7)
		
		#Quit browser.
		print "done."
		time.sleep(3)
		browser.quit()



myClassObject = GetScores()

myClassObject.getAllScores()
