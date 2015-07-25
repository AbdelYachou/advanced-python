#!/usr/python 
# -*- coding: utf-8 -*-

import re

p = r'([A-Z]([a-zñáéíóú ]*)) ([1-9]|0[1-9]|[12][0-9]|3[01])/(Ene|Feb|Mar|Abr|May|Jun|Jul|Ago|Sep|Oct|Nov|Dec)/([2-9]\d\d\d) ([1-9]|0[1-9]|1[12]):([0-9]|[0-5][0-9]) (AM|PM)'

cadenas = ["San Sebastian 31/Ene/2012 11:59 AM",
"Granada 31/Feb/2012 11:59 AM",
"Granada 01/Mar/2012 11:59 PM",
"Granada 1/Abr/2012 11:59 AM",
"Granada 31/May/2012 01:59 AM",
"Granada 31/Jun/2012 1:59 AM",
"Granada 31/Jul/2012 1:9 AM",
"albacete 31/Oct/2012 11:59 AM",
"Gra0ada 31/Feb/2012 11:59 AM",
"Granada 00/Oct/2012 11:59 AM",
"Granada 31/Ele/2012 11:59 AM",
"Granada 31/Ene/1012 11:59 AM",
"Granada 31/Ene/2012 00:59 AM",
"Granada 31/Ele/2012 11:69 AM",
"Granada 31/Ele/2012 11:59 KM"]

def coincide(pattern, string):
    if (re.search(pattern, string) != None):
        print string, "\t Es una fecha valida."
    else:
        print string, "\t No es una fecha valida."

for c in cadenas:
    coincide(p, c)
