no-swayze-no-wayze
==================
This is a multi-function repository. First of all, it functions as a [website](http://www.ahubers.com/no-swayze-no-wayze). Additionally, it will perform data collection by querying Bing for pictures of Patrick Swayze. It then inserts these into a database. These data are used on the website as well as in the subdirectory titled R. There lies the final purpose, analysis on Patrick Swayze color images as well as generating two [Shiny applications](http://shiny.rstudio.com/), [SwayzeStreamApp](http://swayzeallthewayze.shinyapps.io/SwayzeStreamApp), and [SwayzeApp](http://swayzeallthewayze.shinyapps.io/SwayzeApp).  The remaining README will be divided specifically to these seperate purposes.

#Website
##Dependencies
* Python 2.7 running on your web server.
* [PyMySQL](https://github.com/PyMySQL/PyMySQL)

##Files Used
* SwayzeBaby.py - stores all of our Swayze related functions used in this project.
* index.py
* css.css

##Hidden Files
* corner.py - This is a wrapper class for our SQL access, and uses PyMySQL to perform queries, etc. It is not included but has the following format:
```python
import pymysql
#Wrapper for SQL.
class Corner:
	cur = ""
	def __init__(self):
		self.conn = pymysql.connect(user='username',port=3306, passwd='password', host='yourHost', db='yourDatabase')
		self.cur = self.conn.cursor()
	def query(self, query):
		self.cur.execute(query)
```

##How To
Writing your own corner.py and throwing these files on your webserver should make all files run, however you of course would need your own MySQL database filled with Swayzes. So that kind of knicks that idea in the butt.


#Data Collection
##Dependencies
* Python 2.7
* [PyMySQL](https://github.com/PyMySQL/PyMySQL)
* [Bing Search API key](http://datamarket.azure.com/dataset/bing/search)
* [OpenCV](http://opencv.org/)
* [Numpy](http://www.numpy.org/)
* [sklearn](http://scikit-learn.org/stable/)

#Files Used
* SwayzeBaby.py
* collectColors.py
* collectSwayze.py

##Hidden Files
* corner.py (see above)
* keys/key.py - this file has the following format. It's literally just a wrapper for a Bing API key.
```python
class Key:
	def __init__(self):
		return
	def getKey(self):
		key = 'YOUR BING SEARCH API KEY GOES HERE'
		return key
```

##How To
As described above, SwayzeBaby.py is a multi-purpose class for all things Swayze. The remaining two files each populate our tables "swayze"  and "colors". The former contains a url and title tag for each image, while the latter operates on url's from "colors" to run k-means clustering on each image and insert into the DB. Assuming that you have the correct db specifications + a Bing API key, you can run both by uncommenting the imports in SwayzeBaby.py (which have been commented to allow the web page to run).

#Analysis
##Dependencies
* [R](http://www.r-project.org/)
* [Shiny](http://shiny.rstudio.com/)
* [scatterPlot3d](http://cran.r-project.org/web/packages/scatterplot3d/index.html)

##Files Used
* R/SwayzeApp/ (folder)
* R/SwayzeStreamApp/ (folder)

##Hidden Files
No hidden files necessary for these to run. All data stored/loaded from .rdata files. 

##How To
Of all things I've talked about here, this should run out of the box. No hidden files or databases. I suggest you open these folders in [Rstudio](http://www.rstudio.com/), install shiny, and just call `runApp()` in one of the two files mentioned. Play with as desired.
