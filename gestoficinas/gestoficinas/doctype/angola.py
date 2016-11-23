# -*- coding: utf-8 -*-
# Copyright (c) 2016, Helio de Jesus and contributors
# For license information, please see license.txt


from __future__ import unicode_literals
from itertools import ifilter

import frappe
from frappe.utils import nowdate, cstr, flt, cint, now, getdate
from frappe import throw, _
from frappe.utils import formatdate


global suffixes;
suffixes = ["", "thousand", "million", "billion"];
 
global ones;
ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
 
global after_ten;
after_ten = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
 
global tens;
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred"];




UNIDADES = (
    '',
    'UM ',
    'DOIS ',
    'TRES ',
    'QUATRO ',
    'CINCO ',
    'SEIS ',
    'SETE ',
    'OITO ',
    'NOVE ',
    'DEZ ',
    'ONZE ',
    'DOZE ',
    'TREZE ',
    'CATORZE ',
    'QUINZE ',
    'DEZACEIS ',
    'DEZACETE ',
    'DEZOITO ',
    'DEZANOVE ',
    'VINTE '
)

DECENAS = (
    'VINTE ',
    'TRINTA ',
    'QUARENTA ',
    'CINQUENTA ',
    'SESENTA ',
    'SETENTA ',
    'OITENTA ',
    'NOVENTA ',
    'CEM '
)

CENTENAS = (
    'CENTO ',
    'DUZENTOS ',
    'TREZENTOS ',
    'QUATROCENTOS ',
    'QUINHENTOS ',
    'SEISCENTOS ',
    'SETECENTOS ',
    'OITOCENTOS ',
    'NOVECENTOS '
)

UNITS = (
        ('',''),
        ('MIL ','MIL '),
        ('MILLAO ','MILHOES '),
        ('MIL MILHOES ','MIL MILHOES '),
        ('BILLIAO ','BILHOES '),
        ('MIL BILHOES ','MIL BILHOES '),
        ('TRILHAO ','TRILHOES '),
        ('MIL TRILHOES ','MIL TRILHOES '),
        ('QUATRILHAO ','QUATRILHOES'),
        ('MIL QUATRILHOES ','MIL QUATRILHOES '),
        ('QUINTILHAO ','QUINTILHOES '),
        ('MIL QUINTILHOES ','MIL QUINTILHOES '),
        ('SEXTILHAO ','SEXTILHOES '),
        ('MIL SEXTILHOES ','MIL SEXTILHOES '),
        ('SETILHAO ','SETILHOES '),
        ('MIL SETILHOES ','MIL SETILHOES '),
        ('OCTILHAO ','OCTILHOES '),
        ('MIL OCTILHOES ','MIL OCTILHOES '),
        ('NONILLON ','NONILLONES '),
        ('MIL NONILLONES ','MIL NONILLONES '),
        ('DECILLON ','DECILLONES '),
        ('MIL DECILLONES ','MIL DECILLONES '),
        ('UNDECILLON ','UNDECILLONES '),
        ('MIL UNDECILLONES ','MIL UNDECILLONES '),
        ('DUODECILLON ','DUODECILLONES '),
        ('MIL DUODECILLONES ','MIL DUODECILLONES '),
)


MONEDAS = (
    {'country': u'Colombia', 'currency': 'COP', 'singular': u'PESO COLOMBIANO', 'plural': u'PESOS COLOMBIANOS', 'symbol': u'$'},
    {'country': u'Estados Unidos', 'currency': 'USD', 'singular': u'DÓLAR', 'plural': u'DÓLARES', 'symbol': u'US$'},
    {'country': u'Europa', 'currency': 'EUR', 'singular': u'EURO', 'plural': u'EUROS', 'symbol': u'€', 'decimalsingular':u'Céntimo','decimalplural':u'Céntimos'},
    {'country': u'México', 'currency': 'MXN', 'singular': u'PESO MEXICANO', 'plural': u'PESOS MEXICANOS', 'symbol': u'$'},
    {'country': u'Perú', 'currency': 'PEN', 'singular': u'NUEVO SOL', 'plural': u'NUEVOS SOLES', 'symbol': u'S/.'},
    {'country': u'Reino Unido', 'currency': 'GBP', 'singular': u'LIBRA', 'plural': u'LIBRAS', 'symbol': u'£'},
    {'country': u'Angola', 'currency': 'AOA', 'singular': u'Kwanza', 'plural': u'Kwanzas', 'symbol': u'KZ'}
)
# Para definir la moneda me estoy basando en los código que establece el ISO 4217
# Decidí poner las variables en inglés, porque es más sencillo de ubicarlas sin importar el país
# Si, ya sé que Europa no es un país, pero no se me ocurrió un nombre mejor para la clave.

# 
# convert number to words 
# 
def in_words_pt(integer, in_million=True): 
	""" 
	Returns string in words for the given integer. 
	""" 
	n=int(integer) 
 	known = {0: 'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quarto', 5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez', 11: 'onze', 12: 'doze', 13: 'treze', 14: 'catorze', 15: 'quinze', 16: 'dezasseis', 17: 'dezasete', 18: 'dezoito', 19: 'dezanove', 20: 'vinte', 30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 60: 'sessenta', 70: 'setenta', 80: 'oitenta', 90:'noventa'} 


	def psn(n, known, xpsn): 
		import sys; 
		if n in known: return known[n] 
		bestguess, remainder = str(n), 0 

 
		if n<=20: 
			webnotes.errprint(sys.stderr) 
			webnotes.errprint(n) 
			webnotes.errprint("Como isto aconteceu?") 
			assert 0 
		elif n < 100: 
			bestguess= xpsn((n//10)*10, known, xpsn) + '-' + xpsn(n%10, known, xpsn) 
			return bestguess 
		elif n < 1000: 
			bestguess= xpsn(n//100, known, xpsn) + ' ' + 'cem' 
			remainder = n%100 
		else: 
			if in_million: 
				if n < 1000000: 
					bestguess= xpsn(n//1000, known, xpsn) + ' ' + 'mil' 
					remainder = n%1000 
				elif n < 1000000000: 
					bestguess= xpsn(n//1000000, known, xpsn) + ' ' + 'milhões' 
					remainder = n%1000000 
				else: 
					bestguess= xpsn(n//1000000000, known, xpsn) + ' ' + 'bilhões' 
					remainder = n%1000000000 
			else: 
				if n < 100000: 
					bestguess= xpsn(n//1000, known, xpsn) + ' ' + 'mil' 
					remainder = n%1000 
				elif n < 10000000: 
					bestguess= xpsn(n//100000, known, xpsn) + ' ' + 'cem mil' 
					remainder = n%100000 
				else: 
					bestguess= xpsn(n//10000000, known, xpsn) + ' ' + 'dez milhões' 
					remainder = n%10000000 
		if remainder: 
			if remainder >= 100: 
				comma = ',' 
			else: 
				comma = '' 
			return bestguess + comma + ' ' + xpsn(remainder, known, xpsn) 
		else: 
			return bestguess 


	return psn(n, known, psn) 





 
#handles the nomenclature of a triplet
#number: the number in the string form, index: position of the triplet
def gimmeThemWords(number, index):
    length = len(number);
    
    if(length > 3):
        return False;
    
    #pads the number's string representation with 0s on the left
    number = number.zfill(3);
    string = "";
 
    hundreds_digit = ord(number[0]) - 48;
    tens_digit = ord(number[1]) - 48;
    ones_digit = ord(number[2]) - 48;
    
    string += "" if number[0] == '0' else ones[hundreds_digit];
    string += " hundred " if not string == "" else "";
    
    if(tens_digit > 1):
        string += tens[tens_digit - 2];
        string += " ";
        string += ones[ones_digit];
    
    elif(tens_digit == 1):
        string += after_ten[(int(tens_digit + ones_digit) % 10) - 1];
        
    elif(tens_digit == 0):
        string += ones[ones_digit];
        
    #counter check to determine the positional system
    if(string.endswith("zero")):
        string = string[:-len("zero")];
    
    else:
        string += " ";
     
    if(not len(string) == 0):    
        string += suffixes[index];
        
    return string;
    
#initiates the process of converting the number into its cardinal form
def initiateProcess(number):
	length = len(str(number));
	print length
	#counter contains the number of size- 3 groupings of digits that can be formed from the number
	counter = int(length / 3) if length % 3 == 0 else int(length / 3) + 1;
	counter_copy = counter;
	word_representation = [];
 
	for i in range(length - 1, -1, -3):
		print "AQUII"
		word_representation.append(gimmeThemWords(str(number)[0 if i - 2 < 0 else i - 2 : i + 1], counter_copy - counter));
		counter -= 1;
    
	#    print(number,": ", end = " ", flush = True);
	print(number,": ", end );
	for s in reversed(word_representation):
		if(not len(s.strip()) == 0):
			print(s, "", "");
    
	#newline
	print();
 
#number = [7806512341, 7929000401, 901000004009, 234, 2002, 10, 1];

def inicio(number): 
	for n in number:
	    initiateProcess(n);




#=======================




def hundreds_word(number):
	converted = ''
	if not (0 < number < 1000):
		return 'No es posible convertir el numero a letras'

	number_str = str(number).zfill(9)
	cientos = number_str[6:]

	if(cientos):
		if(cientos == '001'):
			converted += 'UN '
		elif(int(cientos) > 0):
			converted += '%s ' % __convert_group(cientos)


	return converted.title().strip()



def __convert_group(n):

	output = ''

	if(n == '100'):
		output = "CEM "
	elif(n[0] != '0'):
		output = CENTENAS[int(n[0]) - 1]

	k = int(n[1:])
	if(k <= 20):
		output += UNIDADES[k]
	else:
		if((k > 30) & (n[2] != '0')):
			output += '%sE %s' % (DECENAS[int(n[1]) - 2], UNIDADES[int(n[2])])
		else:
			output += '%s%s' % (DECENAS[int(n[1]) - 2], UNIDADES[int(n[2])])

	return output

def to_word(number, mi_moneda=None):

	if mi_moneda != None:
		try:
			print "CARRRRRRR"
			print mi_moneda
			print MONEDAS
			moneda = ifilter(lambda x: x['currency'] == mi_moneda, MONEDAS).next()
			print "moeda ", moneda
			if int(number) == 1:
				entero = moneda['singular']
			else:
				entero = moneda['plural']
				if round(float(number) - int(number), 2) == float(0.01):
					fraccion = moneda['decimalsingular']
				else:
					fraccion = moneda['decimalplural']

		except:
			return "Tipo de moneda inválida"
	else:
		entero = ""
		fraccion = ""

	print "POORRRRRRRRRRRRRRRRRRRA"	 	
	human_readable = []
	human_readable_decimals = []
	num_decimals ='{:,.2f}'.format(round(number,2)).split('.') #Sólo se aceptan 2 decimales
	num_units = num_decimals[0].split(',')
	num_decimals = num_decimals[1].split(',')
	#print num_units
	for i,n in enumerate(num_units):
		if int(n) != 0:
			words = hundreds_word(int(n))
			units = UNITS[len(num_units)-i-1][0 if int(n) == 1 else 1]
			human_readable.append([words,units])
	for i,n in enumerate(num_decimals):
		if int(n) != 0:
			words = hundreds_word(int(n))
			units = UNITS[len(num_decimals)-i-1][0 if int(n) == 1 else 1]
			human_readable_decimals.append([words,units])

	#filtrar MIL MILLONES - MILLONES -> MIL - MILLONES
	for i,item in enumerate(human_readable):
		try:
			if human_readable[i][1].find(human_readable[i+1][1]):
				human_readable[i][1] = human_readable[i][1].replace(human_readable[i+1][1],'')
		except IndexError:
			pass
	human_readable = [item for sublist in human_readable for item in sublist]
	human_readable.append(entero)
	for i,item in enumerate(human_readable_decimals):
		try:
			if human_readable_decimals[i][1].find(human_readable_decimals[i+1][1]):
				human_readable_decimals[i][1] = human_readable_decimals[i][1].replace(human_readable_decimals[i+1][1],'')
		except IndexError:
			pass
	human_readable_decimals = [item for sublist in human_readable_decimals for item in sublist]
	human_readable_decimals.append(fraccion)
	sentence = ' '.join(human_readable).replace('  ',' ').title().strip()
	if sentence[0:len('um mil')] == 'Um Mil':
		sentence = 'Mil' + sentence[len('Um Mil'):]
	if num_decimals != ['00']:
		sentence = sentence + ' com ' + ' '.join(human_readable_decimals).replace('  ',' ').title().strip()
	return sentence


def converter():
	print "aaa"
	print to_word(138000)

