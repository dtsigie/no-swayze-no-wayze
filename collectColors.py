#!/usr/bin/env python
import pymysql
from SwayzeBaby import SwayzeBaby
from corner import Corner 

swayze = SwayzeBaby()
selector = Corner()
insertor = Corner()
selector.query("SELECT id, url FROM swayze where fake=0")
for row in selector.cur:
   swayze_id = row[0]
   url = row[1]
   print url
   colors = swayze.getColorScheme(url)
   for color in colors:
	   query = "INSERT INTO colors (swayze_id, color, fake) VALUES ({0}, '{1}', {2})".format(swayze_id, color, 0)
	   insertor.query(query)
				
				

