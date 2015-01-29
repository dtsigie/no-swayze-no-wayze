#!/usr/bin/env python
from SwayzeBaby import SwayzeBaby
from corner import Corner 


swayze = SwayzeBaby()
corner = Corner()
# swaykeys = ['Road%20House', "Ghost", 'point%20Break', 'havana%20nights','dirty%20Dancing']
# swaykeys = ['Road%20House']
for keyword in swaykeys:
	query = "swayze"
	results = swayze.fetchAllSwayze(query)
	for key, value in results.iteritems():
		url = key
		title = value
		query = "INSERT INTO swayze (url, title, fake) VALUES ('{0}', '{1}', {2})".format(url, title, 0)
		corner.query(query)
		break


		# row = SwayzeDB(url=key, title=value)
		# row.save()
	
	# 	for result in data:
	# 		#Make a new instance of our db wrapper.

	# 		corner.query(query)

	# 		id = corner.lastInsert()
	# 		colors = self.getColorScheme(url)

	# 		for (color in colors):
	# 			query = "INSERT INTO colors (swayze_id, color, frequency, fake) VALUES ({0}, '{1}', {2}, {3})".format(lastId, color, 0.0, 0)
	# 			corner.query(query)
				

