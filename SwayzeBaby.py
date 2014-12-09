#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
class SwayzeBaby:
	def __init__(self, image=None):
		if (image):
			self.image = image
		else:
			self.image = self.makeSomeSwayze()

	def makeSomeSwayze(self):
		return
	def getColorScheme(self):
		return ("#000000", "#111111", "#FFFFFF", "#123456")
