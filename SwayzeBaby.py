#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
# import cv2
import urllib2
# import re
# import random

import json
import pprint


class SwayzeBaby:
	def __init__(self, image=None):
		if (image):
			self.image = image
		else:
			self.image = self.makeSomeSwayze()

	def makeSomeSwayze(self):
		data = json.load(urllib2.urlopen('https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=PATRICK%20SWAYZE'))

		pprint.pprint(data)


		# #Stolen from http://www.morwire.com/index.php/python-tutorials/4-scraping-images-from-google
		# url = "https://www.google.ca/search?site=&tbm=isch&q=Patrick+Swayze#q=Patrick+Swayze&tbm=isch"
		# user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
		# #we need to put the user agent into a header format..
		# headers = {'User-Agent':user_agent,}
		  
		# #we also need to put it into the form of a request for urllib2
		# search_request = urllib2.Request(url,None,headers)
		  
		# #now we can request and print the data
		# search_results = urllib2.urlopen(search_request)
		# search_data = search_results.read()
		  
		# #Now we need to parse the data for links
		# #our first step is to compile a regular expression
		# pattern = re.compile('imgurl=([^>]+)&amp;imgrefurl')
		# #now we can search through the data with the new RE
		# image_list = pattern.findall(search_data)
		  
		  
		# #Its time to select a random link until we get a valid image
		# while True:
		# 	#choose a random number..
		# 	index = random.randint(0,len(image_list)-1)
		# 	#create the request for urllib2
		# 	image_request = urllib2.Request(image_list[index],None,headers)
		# 	#make sure its a valid link..
		# 	try:
		# 		image_remote = urllib2.urlopen(image_request)
		# 		if image_remote.headers.maintype == 'image':
		# 			break
		# 	except:
		# 		#this is here just so that we have something..
		# 		index = 0
		# print "<p><img src='" + image_list[index] + "''></p>"

	def getColorScheme(self):
		return ("#000000", "#111111", "#FFFFFF", "#123456")
