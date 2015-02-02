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
print '<link rel="stylesheet" type="text/css" href="css.css">'
# print roadHouse.CSSwayze()
colors = roadHouse.getRandSwayzeColors()
url = colors[0]
color1 = colors[1][0]
color2 = colors[1][1]
color3 = colors[1][2]
print """<style>

#box1 {
	background-color: {0},	
}

#box2 {
	background-color: {1},	
}

#box3 {
	background-color: {2},
}

</style>
""".format(color1, color2, color3)

print "</head>"

#Body stuff.
print "<body>"
print "<div id='container'>"

print "<div id='swayzeImage' align='middle' class='box'>"
print "<img src='" + url + "'></img>" 
print "</div>"

print "<div id='box1' class='box'>"
print "<span class='bigLetters'>ABOUT SWAYZE</span>"
print "</div>"

print "<div id='box2' class='box'>"
print "<span class='bigLetters'>HISTOSWAYZE</span>"
print "</div>"

print "<div id='box3'  class='box'>"
print "<span class='bigLetters'>STREAMSWAYZE</span>"
print "</div>"


# for (color in colors):

	# Print """<img src='{0}' align='middle'></img> """.format(roadHouse.image)
	# Put swayze in center, baby.

print "</div>"
print "</body>"
