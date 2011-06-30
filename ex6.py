#-------------------------------------------------------------------------------
# Name:        ex6.py
# Purpose:
#
# Author:      aaliu
#
# Created:     30/06/2011
# Copyright:   (c) aaliu 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y


hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a righ side."

print w + e