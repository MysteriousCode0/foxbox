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
import sys
import time
import socks
import socket
from modules import style
from modules import scan
from modules import search


# argument parsing
parser = argparse.ArgumentParser(description="Foxbox Penetration Testing Tool")
parser.add_argument("-u", "--url", help="single target url")
parser.add_argument("-d", "--dork", help="dork to use")
parser.add_argument("-f", "--file", help="scans urls from file (with -s)")
parser.add_argument("-s", "--scan", help="scan the url", choices=["sql"])
parser.add_argument("-t", "--tor", help="make requests under tor", action="store_true")
parser.add_argument("-l", "--log", help="log all urls", action="store_true")
parser.add_argument("-v", "--verbose", help="verbose mode", action="store_true")
args = parser.parse_args()


print(style.banner)

def main(dork, scan):

	if not dork == '':
		print("%sUsing the dork: %s%s" %(style.WHITE, style.BLUE, dork))
		url = 'https://search.yahoo.com/search?p=%s' %(dork) 
		search.search(url, scan, log, args.verbose, args.tor)
		if sub == True: 
			print('%sSearching in sub pages...' %(style.WHITE))
			time.sleep(1)
			for page in search.sub_pages:
				search.search(page, scan, log, args.verbose, args.tor)

def extract_url(file):
	# read the dork wordlist 
	with open(file, 'r') as f:
		for url in f.readlines():
			return url.strip('\r').strip('\n')

if __name__ == '__main__':

	if args.tor:
		print("%s[%s#%s] Connecting Tor, please Wait..." %(style.WHITE, style.GREEN, style.WHITE))
		socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050, True)
		socket.socket = socks.socksocket
		print("%s[%s#%s] Connected Successfully, new IP: %s" %(style.WHITE, style.GREEN, style.WHITE,requests.get("http://myexternalip.com/raw").text))
	
	global log

	if args.log:
		open("foxbox_log.txt", 'a+').close()
		log = True
	else:
		log = False
	
	if args.dork:
		global sub
		sub = True
		main(args.dork, args.scan) 

	if args.file:
		for url in extract_url(file):
			if not url[:4] == 'http':
				url = "http://%s" %(url)
			if args.scan:
				scan.sqlscan(url, log, args.tor)
	if args.url:
		if not args.url[:4] == 'http':
			args.url = "http://%s" %(args.url)
		if args.scan:
			scan.sqlscan(args.url, log, args.tor)
