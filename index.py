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
print '<link rel="stylesheet" type="text/css" href="css.css">'
print """<style> 
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
print "</head>"

#Body stuff.
print "<body>"
print """
	<header>
	</header>

"""

print """<img src='{0}' align='middle'></img> """.format(roadHouse.image)
#Put swayze in center, baby.
print "</body>"
