#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
#import cv2
import urllib2
import numpy
# import re
import random

import json
import pprint


class SwayzeBaby:

	swaykeys = ['Road%20House', "Ghost", 'dance', 'point%20Break', 'havana%20nights','dirty%20Dancing']

	def __init__(self, image=None):
		if (image):
			self.image = image
		else:
			self.image = self.makeSomeSwayze()
			while True:
				try:
					image_r = urllib2.urlopen(self.image)
					break
				except:
					self.image = self.makeSomeSwayze()
	
	# Returns an image of Swayze the man Swayze baby.
	def makeSomeSwayze(self):
		#I do not believe Google is too damn keen on me actually performing a google image search.
		#To top that, if you want ot use their API you are limited to 100 calls per day. This method only returns a very short list of
		#the Swayze. But nobody puts baby in the corner... I surely can still get random pictures with sufficiently varied queries!
		swayzeUrl = self.__nobodyPutsBabyInTheCorner()
			
		data = json.load(urllib2.urlopen(swayzeUrl))
		#self.printItems(data, 0)

		luckySwayze = random.randint(0, 3)
		return data['responseData']['results'][luckySwayze]['url']
	#Generates a random Swayze related search query.
	def __nobodyPutsBabyInTheCorner(self):
		swayzeUrl = "https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=PATRICK%20SWAYZE";
		swayzeUrl += "%20"  + random.choice(self.swaykeys)
		start = random.randint(1,30)
		swayzeUrl += "&start={0}".format(start)
		return swayzeUrl

	#Since formatting is hard in html + python.
	def printItems(self, dictObj, indent):
		print '  '*indent + '<ul>\n'
		for k,v in dictObj.iteritems():
			if isinstance(v, dict):
				print '  '*indent , '<li>', k, ':', '</li>'
				self.printItems(v, indent+1)
			else:
				if isinstance(v, list):
					i = 0
					print '  '*indent , '<li>', k, ':', '</li>'
					for item in v:
						print '  '*indent , '<li>', i, ':', '</li>'
						i += 1
						self.printItems(item, indent+1)
						print '</br></br>'
				else:
					print ' '*indent , '<li>', k, ':', v, '</li>'
		print '  '*indent + '</ul>\n'

	#Turns self.image into a histogram to generate. 
	def getColorScheme(self):
		return ("#D5A253", "#301F0D", "#936A4A", "#B85750")
