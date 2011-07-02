#-------------------------------------------------------------------------------
# Name:        ex15.py
# Purpose:
#
# Author:      aaliu
#
# Created:     01/07/2011
# Copyright:   (c) aaliu 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's you file %r:" % filename
print txt.read()

print "I'll also ask you to type it again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()