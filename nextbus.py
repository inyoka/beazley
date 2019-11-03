#!/usr/bin/python3 -dd


import urllib.request

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPrediction.jsp?route=22&stop=14787')
stop = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStop.jsp?route=22&stop=14787')
name = stop.read()


from xml.etree.ElementTree import XML
doc = XML(name)

for pt in doc.findall('.//name'):
    print(pt.text)
