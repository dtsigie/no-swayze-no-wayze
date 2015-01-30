#!/usr/bin/env python # -*- coding: UTF-8 -*-

#import cv2
# enable debugging
import urllib
import urllib2

# import numpy
# import re
import random

import json
# import pprint

#Keep our db stuff wrapped up in a hidden class. We are putting baby in the corner.
from corner import Corner
from keys.key import Key


class SwayzeBaby:
	swaykeys = ['Road%20House', "Ghost", 'dance', 'point%20Break', 'havana%20nights','dirty%20Dancing']

	def __init__(self, image=None):
		return
		# if (image):
		# 	self.image = image
		# else:
		# 	self.image = self.makeSomeSwayze()
		# 	while True:
		# 		try:
		# 			image_r = urllib2.urlopen(self.image)
		# 			break
		# 		except:
		# 			self.image = self.makeSomeSwayze()
	
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
	# def printItems(self, dictObj, indent=" "):
	# 	print '  '*indent + '<ul>\n'
	# 	for k,v in dictObj.iteritems():
	# 		if isinstance(v, dict):
	# 			print '  '*indent , '<li>', k, ':', '</li>'
	# 			self.printItems(v, indent+1)
	# 		else:
	# 			if isinstance(v, list):
	# 				i = 0
	# 				print '  '*indent , '<li>', k, ':', '</li>'
	# 				for item in v:
	# 					print '  '*indent , '<li>', i, ':', '</li>'
	# 					i += 1
	# 					self.printItems(item, indent+1)
	# 					print '</br></br>'
	# 			else:
	# 				print ' '*indent , '<li>', k, ':', v, '</li>'
	# 	print '  '*indent + '</ul>\n'

	#Turns self.image into a histogram to generate. 
	def getColorScheme(self, url):

            req = urllib.urlopen(url)
            arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
            img = cv2.imdecode(arr,-1)

            # load the image and convert it from BGR to RGB
            image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


            # reshape the image to be a list of pixels
            image = image.reshape((-1, 3))

                # cluster the pixel intensities
            clt = KMeans(n_clusters = 4)
            clt.fit(image)

                # build a histogram of clusters and then create a figure
                # representing the number of pixels labeled to each color
            hist = centroid_histogram(clt)
            hist = clt.cluster_centers_
            colors = list()
            for x in range(0,4):
                        r = hist[x][0].astype(np.int64)
                        g = hist[x][1].astype(np.int64)
                        b = hist[x][2].astype(np.int64)
                        hex = "#{0:02x}{1:02x}{2:02x}".format(clamp(r), clamp(g), clamp(b))
                        colors.append(hex)        



            # show our color bart
                return colors



        def centroid_histogram(clt):
                # grab the number of different clusters and create a histogram
                # based on the number of pixels assigned to each cluster
                numLabels = len(np.unique(clt.labels_))
                (hist, _) = np.histogram(clt.cluster_centers_, bins = numLabels)
                

                # normalize the histogram, such that it sums to one
                hist = hist.astype("float")
                hist /= hist.sum()

                # return the histogram
                return hist

##      Helper function for string formatting
        def clamp(x): 
          return max(0, min(x, 255))


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

	# Retruns an image dictionary with image url as key and title as values - collected from bing search
	def fetchAllSwayze(self, query):
		ourKey = Key()
		key = ourKey.getKey()
		
		query = urllib.quote(query)
		skip = 0
		imageDict = {}
		while True:
			 # create credential for authentication
			user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
			credentials = (':%s' % key).encode('base64')[:-1]
			auth = 'Basic %s' % credentials
			url = 'https://api.datamarket.azure.com/Data.ashx/Bing/Search/Image?$top=50&$format=json&$skip='+ str(skip) + '&Query=%27' + query +'%27'
			request = urllib2.Request(url)
			request.add_header('Authorization', auth)
			request.add_header('User-Agent', user_agent)
			request_opener = urllib2.build_opener()
			response = request_opener.open(request) 
			response_data = response.read()
			json_result = json.loads(response_data)
			result_list = json_result['d']['results']
			 #extracts results from each page
			
			#print result_list[5]['Title']
			# print result_list[49]['MediaUrl']
			try:
				for i in range (0,49):
					title = result_list[i]['Title']
					imageUrl = result_list[i]['MediaUrl']
					imageDict[imageUrl] = title
				skip +=50
				if skip > 1000:
					break
			except(IndexError):
				return imageDict

		
		
		#print imageDict
		return imageDict


				
				
			
