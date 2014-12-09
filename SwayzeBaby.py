#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
# import cv2
import urllib2
# import re
import random

import json
import pprint


class SwayzeBaby:

	makeSomeBabies = ['Road%20House', "Ghost", 'dance', 'point%20Break', 'havana%20nights','actor','dirty%20Dancing','celebrity','image','muscles']

	def __init__(self, image=None):
		if (image):
			self.image = image
		else:
			self.image = self.makeSomeSwayze()
	
	# Returns an image of Swayze the man Swayze baby.
	def makeSomeSwayze(self):
		#I do not believe Google is too damn keen on me actually performing a google image search.
		#To top that, if you want ot use their API you are limited to 100 calls per day. This method only returns a very short list of
		#the Swayze. But hell, nobody puts baby in the corner... I surely can still get random pictures with sufficiently varied queries!
		swayzeUrl = self.__nobodyPutsBabyInTheCorner()
			
		data = json.load(urllib2.urlopen(SwayzeUrl))
		print json.dumps(jsonStr, sort_keys=True, indent=2, separators=(',', ': '))

	#Generates a random Swayze related search query.
	def __nobodyPutsBabyInTheCorner(self):
		swayzeUrl = "https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=PATRICK%20SWAYZE";
		howManyBabies = random.randInt(0,len(makeSomeBabies))
		for i in range(1, howManyBabies):
			swayzeUrl += "%20"  + random.choice(makeSomeBabies)
		return swayzeUrl



	#Turns self.image into a histogram to generate. 
	def getColorScheme(self):
		return ("#000000", "#111111", "#FFFFFF", "#123456")
