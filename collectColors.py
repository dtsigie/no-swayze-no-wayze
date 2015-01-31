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
   colors = swayze.getColorScheme(url)
   for color in colors:
	   query = "INSERT INTO colors (swayze_id, color) VALUES (%s, %s)"
	   insertor.cur.execute(query, (swayze_id, color) )				
				

