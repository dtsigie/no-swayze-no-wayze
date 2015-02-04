no-swayze-no-wayze
==================
This is a multi-function repository. First of all, it functions as a [website](ahubers.com/no-swayze-no-wayze). Additionally, it will perform data collection by querying Bing for pictures of Patrick Swayze. It then inserts these into a database. These data are used on the website as well as in the subdirectory titled R. There lies the final purpose, analysis on Patrick Swayze color images as well as generating two [Shiny applications](http://shiny.rstudio.com/), [SwayzeStreamApp](http://swayzeallthewayze.shinyapps.io/SwayzeStreamApp), and [SwayzeApp](http://swayzeallthewayze.shinyapps.io/SwayzeApp).  The remaining README will be divided specifically to these seperate purposes.

#Website
##Dependencies
*Python running on your web server.
*[PyMySQL](https://github.com/PyMySQL/PyMySQL)

##Files Used
SwayzeBaby.py
index.py
css.css

##How To
Writing your own corner.py and throwing these files on your webserver should make all files run, however you of course would need your own MySQL database filled with Swayzes. So that kind of knicks that idea in the butt.

##Hidden Files
*corner.py - This is a wrapper class for our SQL access, and uses PyMySQL to perform queries, etc. It is not included but has the following format:
```
import pymysql
#Wrapper for SQL.
class Corner:
	cur = ""
	def __init__(self):
		self.conn = pymysql.connect(user='username',port=3306, passwd='password', host='yourHost', db='yourDatabase')
		self.cur = self.conn.cursor()
	def query(self, query):
		self.cur.execute(query)
	def lastInsert(self):
		query = "SELECT LAST_INSERT_ID() as id;"
		result = self.query(query)
		return result

```


#Data Collection


#Analysis
