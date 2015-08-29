#!/usr/bin/env python # -*- coding: UTF-8 -*-

#import cv2, the sklearn kmeans function, and numpy
#from sklearn.cluster import KMeans
#import numpy as np
#import cv2
##enable debugging
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

	def getRandSwayzeColors(self):
		# return ['http://home.comcast.net/~patrick.swayze/patrickcloseup.jpg', "#123456", "#223344", "445566"]
		corner = Corner()

		query = """
		SELECT swayze_id FROM colors WHERE fake = 0
		ORDER BY RAND()
		LIMIT 1
		"""

		corner.cur.execute(query)

		for row in corner.cur:
			swayze_id = row[0]

		query = "SELECT swayze.url, colors.color FROM swayze INNER JOIN colors ON swayze.id = colors.swayze_id WHERE swayze_id = " + str(swayze_id) 

		corner.cur.execute(query)
		colors = []
		for row in corner.cur:
			url = row[0]
			colors.append(row[1])
		return [url, colors]



	def getDuplicateSwayze(self):
		query = """
		  select url, count(*)
		  from swayze
		  group by url
		  having count(*) > 1
		"""

		corner = Corner()
		corner.cur.execute(query)

	#Turns self.image into a histogram to generate. 
	def getColorScheme(self, url):
	# try-catch for error detection, allowing us to bypass bad URLs and other errors
                try: 
				# pull a picture from a URL, turn it to a bytearray, then decode it for analysis
                        req = urllib2.urlopen(url)
                        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
                        img = cv2.imdecode(arr,-1)

                        # load the image and convert it from BGR to RGB
                
                        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        # reshape the image to be a list of pixels
                        image = image.reshape((-1, 3))

                                # cluster the pixel intensities into 3 clusters
                        clt = KMeans(n_clusters = 3)
                        clt.fit(image)

                                # build a histogram of clusters and then store the centroids of these clusters in a list
                        hist = centroid_histogram(clt)
                        hist = clt.cluster_centers_
                        colors = list()
                        for x in range(0,3):
                                r = hist[x][0].astype(np.int64)
                                g = hist[x][1].astype(np.int64)
                                b = hist[x][2].astype(np.int64)
                                hex = "#{0:02x}{1:02x}{2:02x}".format(clamp(r), clamp(g), clamp(b))
                                colors.append(hex)        



                        # return the colors in hex format
                        return colors
		except (urllib2.HTTPError, urllib2.URLError, Exception, cv2.error) as e:

                        print("Image processing failed. Moving on...")
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
			
