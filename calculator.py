#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Calculadora

Para ejecutarlo, desde la shell:
$ python calculator.py función operando1 operando2

Las funciones disponibles son: sum, rest, mult y div

"""

import sys

if len(sys.argv) != 4:
	print
	sys.exit("Invalid arguments")
try:
	if sys.argv[1] == "sum":
		Sol = float(sys.argv[2]) + float(sys.argv[3]) 
	elif sys.argv[1] == "rest":
		Sol = float(sys.argv[2]) - float(sys.argv[3])
	elif sys.argv[1] == "mult":
		Sol = float(sys.argv[2]) * float(sys.argv[3])
	elif sys.argv[1] == "div":
		Sol = float(sys.argv[2]) / float(sys.argv[3])
except ZeroDivisionError:
	print "Error: Division by zero"
else:
	print Sol

