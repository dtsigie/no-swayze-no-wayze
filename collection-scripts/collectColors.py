#!/usr/bin/env python
import pymysql
from SwayzeBaby import SwayzeBaby
from corner import Corner
#Here's a counter to count how many images we've processed
x = 1
   
#instantiate our objects 
swayze = SwayzeBaby()
selector = Corner()
insertor = Corner()
startId = 0
selector.query("SELECT id, url FROM swayze where fake=0 AND id >= " + repr(startId))
for row in selector.cur:
   swayze_id = row[0]
   url = row[1]
   colors = swayze.getColorScheme(url)
   if colors is None:
         print("fuck that image")
   else:
      for color in colors:
         query = "INSERT INTO colors (swayze_id, color) VALUES (%s, %s)"
         insertor.cur.execute(query, (swayze_id, color) )
         print("Processed " + repr(x/3) + " images. Last printed: " + repr(swayze_id))
         x += 1   
				

