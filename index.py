#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()
from SwayzeBaby import SwayzeBaby
print "Content-Type: text/html\n\n"
roadHouse = SwayzeBaby()

print "<head>"
print "<link rel='shortcut icon' href='favicon.ico' type='image/x-icon'/ >"
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
print "<div id='topLayer'>"

print "<div id='swayzeImage' align='middle'>"
print "<a href=''><img src='" + url + "'></img></a>" 
print "</div>"

print "<div id='title' class='bigLetters'>"
print "<span>NO SWAYZE NO WAYZE</span>"
print "</div>"
print "<hr></hr>"
print "<div id='subtitle'/>"
print "<p style='font-size:250%'>Swayze based color schemes, analysis, and data viz</p>"
print "</div>"

print "<div class='mainText'>"
#This stuff was only really for handing the project in.
print """<p>Brian Hixson-Simeral, Alex Hubers, Kent Schlorf, Dawit Tsigie</p>
<p>Cornell College. Mount Vernon, IA.</p>
<ul>"""
#<li class='download, orange'><a href='fullWriteUp.pdf'>full write-up</a> </li>
#<li class='blue'><a href='https://docs.google.com/presentation/d/1Vr0AP1aMLPH6XotAbR5BTNFdEmlsRMAeUcv5vHSvJQ4/edit?usp=sharing'>presentation slides</a> </li>"""

print """
<li class='green'><a href='https://github.com/ahubers/no-swayze-no-wayze'>source code</a></li>
<li class='purple'><a href='http://swayzeallthewayze.shinyapps.io/SwayzeApp'>data visualization</a></li>
<li class='gold'><a href='http://swayzeallthewayze.shinyapps.io/SwayzeStreamApp'>stream graph</a></li>
<ul>"""
print "</div>"
print "</div>"

print '<div id="revealed-section-placeholder"></div>'
print "<div id='revealed-section'>"
print "<div id='box1' class='box'>"
print "<div class='textBox'>"
print "<p class='bottomRight'>{0}</p>".format(color1)
print "</div>"
print "</div>"

print "<div id='box2' class='box'>"
print "<div class='textBox'>"
print "<p class='bottomRight'>{0}</p>".format(color2)
print "</div>"
print "</div>"

print "<div id='box3'  class='box'>"
print "<div class='textBox'>"
print "<p class='bottomRight'>{0}</p>".format(color3)
print "</div>"
print "</div>"

print "</div>"

print "</div>"
print "</body>"
