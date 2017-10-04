from word_list import *

# l = ['alberto','miguel','raul','samuel','wolverine']
# l = ['perro', 'gatico', 'peluca']

no_hibrid_list = process_file('Mujeres2.txt',skip_header=False)

def password_maker(li, dash=True, count=True, undera=True, simbol=True, under_simbol=True, capitaliz=True, rang=10000, simbols='+/$!@#$%^&*()'):

	# dash =
	# count =
	# undera = 
	# simbol = 
	# under_simbol = 
	# capitaliz = 

	diccionario = dict()

	for word in li:
		capitalized = []
		counted = []
		undered = []
		dashed = []
		simbolx = []
		u_simbol = []

		if capitaliz:
			capitalized = capitalize(word,rang)

		if count:

			counted = counter(word,rang)
			
		if undera:
			undered = under(word,rang)

		if simbol:
			simbolx = add_simbol(word,rang,simbols)

		if under_simbol:
			u_simbol = add_under_simbol(word,rang,simbols)

		if dash:
			dashed = add_dash(word,rang)


		total = capitalized + counted + undered + simbolx + u_simbol + dashed


		diccionario[word] = total

	return diccionario


def capitalize(word,rang):
	l = []
	word = word.title()

	for i in range(rang):

		l.append(word + str(i))   

	return l

def counter(word,rang):
	l = []
	for i in range(rang):

		l.append(word + str(i))   

	return l

def add_simbol(word,rang,simbol):
	l = []
	# simbol = '!@%^&*()'
	for s in simbol:
		for i in range(rang):

			l.append(word + str(i) + s)   

	return l

def under(word,rang):
	l = []
	for i in range(rang):
		l.append(word + '_' + str(i))
	return l


def add_under_simbol(word,rang,simbol):
	l = []
	# simbol = '!@%^&*()'
	for s in simbol:
		for i in range(rang):

			l.append(word + '_' + str(i) + s)   

	return l

def add_dash(word,rang):
	l = []
	for i in range(rang):
		l.append(word + '-' + str(i))

	return l 


def key_list(diccionario):
	'''Genera una lista con las llaves del diccionario'''
	keys = diccionario.keys()

	return sorted(keys)

def key_print(diccionario):
	'''Imprime una lista con las llaves del diccionario'''
	for key in key_list(diccionario):
		print key

def diccio_to_list(diccionario):
	'''Pasa los valores de un diccionario a una lista'''

	l = []

	for value, key in diccionario.items():
		l.append(value)
		for item in key:
			l.append(item)
	return l


def open_file(lista):
	'''Procesa la lista y crea un archivo txt con todas los items'''

	password_txt = open("Hibrido.txt", "w")

	for item in lista:

		password_txt.write(item + '\n')

	password_txt.close() 





name_dict =  password_maker(no_hibrid_list)

# # #Imprime la lista de llaves por orden alfabetico
# # key_print(name_dict)

# #Imprimer todo el diccionario
# # print name_dict

# # #Imprime todas las variaciones de una clave 
# # # print name_dict['amarilis']

lista_hibrida = diccio_to_list(name_dict)

open_file(lista_hibrida)

