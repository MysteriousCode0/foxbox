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

import sys
import socks
import socket
import requests
from modules import style


def sqlscan(url, log, tor):
	if tor:
		socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050, True)
		socket.socket = socks.socksocket
	vuln = False
	payloads = ['\'', '"'] 
	errors = ['You have an error in your SQL syntax', 'mysql_num_rows()'] 
	try:
		for payload in payloads: 
			for error in errors: 
				if error in requests.get(url + payload).text: 
					vuln = True 
		if vuln:
			print("%sFound SQL injection: %s%s" %(style.WHITE, style.GREEN, url))
			if log:
				logger(url)
		else: 
			print("%sSQL injection not Found: %s%s" %(style.WHITE, style.RED, url))
	except KeyboardInterrupt:
		sys.exit()
	except Exception as e:
		#print(e)
		pass

def logger(data):
	f = open("sqli.txt", 'a+')
	f.write(data + "\n")
	f.close()
