# Foxbox Penetration Testing Tool

Foxbox is a simple and powerfull Penetration Testing Tool.
This tool allows you to find and scan urls by using dorks.
Last version: 1.2

# Usage:

*usage: foxbox.py [-h] [-u URL] [-d DORK] [-f FILE] [-s {sql}] [-t] [-l] [-v]

*Foxbox Penetration Testing Tool

*optional arguments:
*  -h, --help            show this help message and exit
*  -u URL, --url URL     single target url
*  -d DORK, --dork DORK  dork to use
*  -f FILE, --file FILE  scans urls from file (with -s)
*  -s {sql}, --scan {sql}
*                        scan the url
*  -t, --tor             make requests under tor
*  -l, --log             log all urls
*  -v, --verbose         verbose mode
*


# Example of usage:

*./foxbox.py -d <your dork> -s sql -t

