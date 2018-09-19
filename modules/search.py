'''
- Foxbox Penetration Testing Tool

- Foxbox is and easy and powerful Penetration Testing tool 
- which allows you to find and scan urls by using dorks.

- This tool is for Educational purposes only.
- Developers assume no liability and are not responsable
- for any misuse or damage caused by this program.

- Coded by RoadToHacker
- Instagram: road.to.hacker
'''


import argparse 
import requests
import re
import sys
import bs4
import time
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse
from modules import style
from modules import scan


def search(url, scan_type, log, verbose, tor):

	global sub_pages
	sub_pages = [] 
	try:
		source = requests.get(url).text 
		soup = bs(source, 'lxml')
		for link in soup.find_all('a'):
			link = link.get('href')
			if log:
				logs = open("foxbox_log.txt", 'r') 
			if link[:4] == 'http': 
				if "cc.bing" in link:
					pass
				elif "yahoo" in link:
					if link[:14] == 'https://search': 
						sub_pages.append(link) 
				else:
					if log:
						if not link + "\n" in logs: 
							pass					
					if scan_type == 'sql': 
						if not urlparse(link).query == '': 
							scan.sqlscan(link, log, tor) 
						else:
							if verbose:
								print('%sQuery not Found: %s%s' %(style.WHITE, style.RED, link)) 
					else:
						print('%sFound %s%s'%(style.GREEN, style.WHITE, link)) 
					if log:
						logger(link) 
			if log:
				logs.close() 

	except KeyboardInterrupt:
		exit()


def logger(data):
	f = open("foxbox_log.txt", 'a+')
	f.write(data + "\n")
	f.close()
