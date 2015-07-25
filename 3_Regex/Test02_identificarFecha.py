#!/usr/python
# -*- coding: utf-8 -*-

import re

# Patron para reconocer fechas

patron = "([A-Z]([a-zñáéíóú ]*)) ([1-9]|0[1-9]|[12][0-9]|3[01])/(Ene|Feb|Mar|Abr|May|Jun|Jul|Ago|Sep|Oct|Nov|Dec)/([2-9]\d\d\d) ([1-9]|0[1-9]|1[12]):([0-9]|[0-5][0-9]) (AM|PM)"

print patron

# Lo probamos
cadenas =[
"San Sebastian 5/Ago/2012 2:23 AM",
"San Sebastian 5/Ago/2012 2:23 TM",
"Sebastian 05/Ago/2012 02:3 AM",
"San Sebastian 5/Aga/2012 02:23 AM", 
"San Sebastian de los Reyes 05/Ago/2012 02:23 AM", 
"San Sebastian 5/Ago/1912 2:23 AM", 
"San Sebastian 005/Ago/2012 02:23 AM", 
]
 # Correcta
 # TM
 # Correcta
 # Aga
 # Correcta
 # 1912
 # 005
 
for c in cadenas:
	if re.search(patron, c):
		print c+" -> Correcta"
	else:
		print c+" -> Incorrecta"
