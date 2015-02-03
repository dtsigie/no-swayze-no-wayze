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

#box1 {{
	background-color: {0};	
}}

#box2 {{
	background-color: {1};	
}}

#box3 {{
	background-color: {2};
}}

</style>
""".format(color1, color2, color3)

print "</head>"

#Body stuff.
print "<body>"
print "<div id='container'>"


print "<div id='swayzeImage' align='middle' class='box'>"
print "<img src='" + url + "'></img>" 
print "</div>"

print "<div id='title' class='bigLetters'>"
print "<span>NO SWAYZE NO WAYZE</span>"
print "</div>"
print "<hr></hr>"
print "<div id='subtitle'/>"
print "<p style='font-size:250%'>Swayze based color schemes for the web</p>"
print "</div>"


print "<div id='box1' class='box'>"
print "<span class='bigLetters'>ABOUT</span>"
print "<div class='mainText'>"
print """<p>No Swayze No Wayze is the attractive brainchild of Cornell College (Mount Vernon, IA) students Alex Hubers, Brian 
Hixson-Simeral, Kent Schlorf, and Dawit Tsigie. Click below for more details. </p>
<ul>
<li><a href='fullWriteUp.pdf'>Full Write-up</a> </li>
<li><a href='https://github.com/ahubers/no-swayze-no-wayze'>Source Code</a> </li>
<li><a href='https://docs.google.com/presentation/d/1Vr0AP1aMLPH6XotAbR5BTNFdEmlsRMAeUcv5vHSvJQ4/edit?usp=sharing'>Presentation Slides</a> </li>
<ul>"""
print "</div>"
print "<div class='textBox'>"
print "<p class='bottomRight'>{0}</p>".format(color1)
print "</div>"
print "</div>"

print "<div id='box2' class='box'>"
print "<span class='bigLetters'><a href='http://swayzeallthewayze.shinyapps.io/SwayzeApp'>DATA VIZ</a></span>"
print "<div class='textBox'>"
print "<p class='bottomRight'>{0}</p>".format(color2)
print "</div>"
print "</div>"

print "<div id='box3'  class='box'>"
print "<span class='bigLetters'><a href='http://swayzeallthewayze.shinyapps.io/SwayzeStreamApp'>SWAYZE STREAM</a></span>"
print "<div class='textBox'>"
print "<p class='bottomRight'>{0}</p>".format(color3)
print "</div>"
print "</div>"


# for (color in colors):

	# Print """<img src='{0}' align='middle'></img> """.format(roadHouse.image)
	# Put swayze in center, baby.

print "</div>"
print "</body>"
