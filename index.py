#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()
from SwayzeBaby import SwayzeBaby
print "Content-Type: text/html\n\n"
print

roadHouse = SwayzeBaby()
colorScheme = roadHouse.getColorScheme()

print "<head>"
print "<title>No Swayze No Wayze</title>"

print """<style> 
	body {{
		background: repeating-linear-gradient(
			to right,
			{0} 100px,
			{1} 100px,
			{2} 100px,
			{3} 100px,
		);
	}}
	</style>""".format(colorScheme[0], colorScheme[1], colorScheme[2], colorScheme[3])
print "</head>"

#Body stuff.
print "<body>"

print """<img src='{0}'></img> """.format(roadHouse.image)
#Put swayze in center, baby.
print "</body>"
