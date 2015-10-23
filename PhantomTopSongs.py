import re
import mechanize
from selenium import webdriver
import time
import csv

class GetPlaylist(object):

	def getTopSongs(self):
		print "working Billboard.."
		browser = webdriver.PhantomJS('c:/PhantomJS/bin/phantomjs.exe')
		
		#Opens our webpage and waits...
		browser.get('http://www.billboard.com/charts/rock-songs')
		time.sleep(5)
		
		#Grab what we need and make it a variable. Print output and quit browser.
		
		# title = browser.find_element_by_xpath('//div[@class="row-title"]').text
		x = 1
		while (x < 11):
			title = browser.find_element_by_xpath('//article[@id="row-'+str(x)+'"]').text
			print title
			
			#WRITE/APPEND TO CSV HERE
			x+=1
		
		
		time.sleep(3)
		browser.quit()
		
myClassObject = GetPlaylist()

myClassObject.getTopSongs()
