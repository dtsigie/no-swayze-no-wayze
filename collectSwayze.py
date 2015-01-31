#!/usr/bin/env python
from SwayzeBaby import SwayzeBaby
from corner import Corner
import urllib 

swayze = SwayzeBaby()
corner = Corner()
swaykeys = ["",  "Skatetown, U.S.A.", "The Outsiders","Uncommon Valor","Grandview, U.S.A. ","Red Dawn ","Youngblood ","Dirty Dancing ","Steel Dawn ","Tiger Warsaw ","Road House ","Next of Kin ","Ghost ","Point Break ","City of Joy ","Father Hood ","Tall Tale ","To Wong Foo Thanks for Everything, Julie Newmar ","Three Wishes ","Black Dog ","Letters from a Killer ","Forever Lulu ","Green Dragon ","Donnie Darko ","Waking Up in Reno ","One Last Dance ","11:14 ","Dirty Dancing: Havana Nights ","Keeping Mum ","The Fox and the Hound 2 ","Jump! ","Christmas in Wonderland ","Powder Blue "]
swaykeys = ["Letters from a Killer ","Forever Lulu ","Green Dragon ","Donnie Darko ","Waking Up in Reno ","One Last Dance ","11:14 ","Dirty Dancing: Havana Nights ","Keeping Mum ","The Fox and the Hound 2 ","Jump! ","Christmas in Wonderland ","Powder Blue "]
# swaykeys = [""]
for keyword in swaykeys:
	query = "swayze " + keyword
	results = swayze.fetchAllSwayze(query)
	for key, value in results.iteritems():
		url = key
		title = value
		# url = urllib.unquote(url)
		# title = urllib.unquote(title)
		# title = title.encode('ascii', 'ignore')
		# title = title.replace('"', '\\"')
		# title = title.replace("'", "\\'")
		query = "INSERT INTO swayze (url, title) VALUES (%s, %s)"
		corner.cur.execute(query, (url, title ) )

