#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()
from SwayzeBaby import SwayzeBaby
print "Content-Type: text/html\n\n"
print
roadHouse = SwayzeBaby()

print "<head>"
print "<title>No Swayze No Wayze</title>"
# print '<link rel="stylesheet" type="text/css" href="css.css">'
# print roadHouse.CSSwayze()
print "</head>"

#Body stuff.
print "<body>"
print "<div id='container'>"
colors = roadHouse.getRandSwayzeColors()
	# print """<img src='{0}' align='middle'></img> """.format(roadHouse.image)
	#Put swayze in center, baby.

print "</div>"
print "</body>"
