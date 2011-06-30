#-------------------------------------------------------------------------------
# Name:        ex8.py
# Purpose:
#
# Author:      aaliu
#
# Created:     30/06/2011
# Copyright:   (c) aaliu 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter %(
    "I had this thing.",
    "That you could type up righ.",
    "But it didn't sing.",
    "So I said goodnight.")