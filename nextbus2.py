#!/usr/bin/env python3
import sys


'''
Notes : 

Sample data for command line args :
    6 5037
    22 14791
Commands used but deleted :
    print('Command options:', route, stopid)
    raise SystemExit(0) # Halt program
    u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPrediction.jsp?route=22&stop=14787')
Debegging using Python DeBugger
import pdb
pdb.pm() # pm = post mortum

or 

import pdb; pdb.set_trace() # Launch Debugger

'''

if len(sys.argv) != 3 :
    raise SystemExit('Usage: nextbus.py route stopid')

route = sys.argv[1]
stopid = sys.argv[2]

import urllib.request

stop = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStop.jsp?route={}&stop={}'.format(route,stopid))
name = stop.read()


from xml.etree.ElementTree import XML
doc = XML(name)

for pt in doc.findall('.//name'):
    print(pt.text)

