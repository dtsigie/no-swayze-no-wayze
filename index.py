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
	.roadHouse {{ 
		color: {0}; 
	}} 
	.dirtyDancing {{ 
		color: {1}; 
	}} 
	.pointBreak {{ 
		color: {2}; 
	}} 
	.ghost {{ 
		color: {3}; 
	}} 
	</style>""".format(colorScheme[0], colorScheme[1], colorScheme[2], colorScheme[3])
print "</head>"

#Body stuff.
print "<body>"
#Put swayze in center, baby.
print "</body>"
