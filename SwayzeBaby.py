#!/usr/bin/env python # -*- coding: UTF-8 -*-

#import cv2
# enable debugging
import urllib2
import numpy
# import re
import random

import json
import pprint

#Keep our db stuff wrapped up in a hidden class. We are putting baby in the corner.
from corner.py import Corner


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
	def getColorScheme(self, url):
		return ("#D5A253", "#301F0D", "#936A4A", "#B85750")

	#Returns out html-parseable css involving our color schemes.
	def CSSwayze(self):
		colorScheme = self.getColorScheme()
		css = """<style> 
		body {{
			background-image: linear-gradient(
				to right,
				{0},
				{0} 25%,
				{1} 25%,
				{1} 50%,
				{2} 50%,
				{2} 75%,
				{3} 75%
			);
		background-size: 100% 100%;
		}}
		</style>""".format(colorScheme[0], colorScheme[1], colorScheme[2], colorScheme[3])

		return css

	#Takes in a data dictionary and inserts that into our database. Called from the data collection function.
	def penetrateSwayze(self, data):
		for result in data:
			#Make a new instance of our db wrapper.
			corner = new Corner()
			url = result['url']
			title = result['title']

			query = "INSERT INTO swayze (url, title, fake) VALUES ('{0}', '{1}', {2})".format(url, title, 0)
			corner.query(query)

			id = corner.lastInsert()
			colors = self.getColorScheme(url)

			for (color in colors):
				query = "INSERT INTO colors (swayze_id, color, frequency, fake) VALUES ({0}, '{1}', {2}, {3})".format(lastId, color, 0.0, 0)
				corner.query(query)
				
				
			
