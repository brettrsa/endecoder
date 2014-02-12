#!/usr/bin/python
#
# A simple encoder/decoder
#
# Start

import sys

if len(sys.argv) > 1:

        action = sys.argv[1]
	type = sys.argv[2]
	string = sys.argv[3]

	if action == 'decode':
   	      data = string.decode(type)
   	      print data
	elif action == 'encode':
   	     data = string.encode(type)
   	     print data
else:
	print '-------------------------------------------------------'
        print 'Usage: ./endecoder.py <encode/decode> <type> <string> '
        print '-------------------------------------------------------'
	print 'Example : '
 	print "./endecoder.py encode base64 'hello world of mayhem'"
        print '-------------------------------------------------------'
# End

