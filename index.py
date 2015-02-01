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
print "</head>"

#Body stuff.
print "<body>"
print "<div id='container'>"
colors = roadHouse.getRandSwayzeColors()
url = colors[0]
color1 = colors[1]
color2 = colors[2]
color3 = colors[3]
print "<div id='swayzeImage' align='middle' class='box'>"
print "<img src='" + url + "'></img>" 
print "</div>"

print "<div id='box1' class='box'>"
print "<span class='bigLetters'>ABOUT SWAYZE</span>"
print "</div>"

print "<div id='box2' class='box'>"
print "<span class='bigLetters'>HISTOSWAYZE</span>"
print "</div>"

print "<div id='box3' class='box'>"
print "<span class='bigLetters'>STREAMSWAYZE</span>"
print "</div>"


# for (color in colors):

	# Print """<img src='{0}' align='middle'></img> """.format(roadHouse.image)
	# Put swayze in center, baby.

print "</div>"
print "</body>"
