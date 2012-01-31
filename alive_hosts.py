#!/usr/bin/env python

import httplib
import sys

def Usage():
	print "Usage: Python <python scipt> [host] [port] [path, like '/']"


def main() :
	req_host = sys.argv[1]
	port = int(sys.argv[2])
	path = sys.argv[3]	
	
	host = httplib.HTTPConnection(req_host , port)
	host.request('GET' , path)
	resp = host.getresponse()
	
	#print resp	
	print "Here is the HTTP Response ..."
	print
	print "		Status  = " , resp.status
	print "		Reason  = " , resp.reason
	print
	print "And this is the header that we got .."
	
	#print resp.getheaders()
	print
	for  field , val in resp.getheaders():
		print "	%s: %s" %(field , val)

if __name__ == '__main__':
	if len(sys.argv) < 3:
		Usage()
	else:
		main()


