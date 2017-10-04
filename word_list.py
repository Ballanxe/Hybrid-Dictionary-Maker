import string
import random
# import word_filter
# from password_maker_p import *

def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
   
    Returns: map from each word to the number of times it appears.
    """
    lista = []
    book = file(filename)

    if skip_header:
        skip_gutenberg_header(book)

    for line in book:
        process_line(line, lista)

    lista3 = word_filter(lista)

    return lista3


def word_filter(lista):
    '''Genera una lista sin repetir limpia sin palabras repetidas'''
    lista2 = []
    for word in lista:
        if check_word(lista2, word):
            continue
        else:
            lista2.append(word) 
    return lista2 


def check_word(lista, word):
    '''Verifica si una palabra se encuentra repetida'''
    if word in lista:
        return True
    else:
        return False  


def skip_gutenberg_header(book):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in book:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def process_line(line, lista):
    """Adds the words in the line to the histogram.

    Modifies hist.

    line: string
    hist: histogram (map from word to frequency)
    """
    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')
    
    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        # update the histogram
        # hist[word] = hist.get(word, 0) + 1
        lista.append(word)

def keySorter(l2):
     print sorted(l2)


# #genera una lista de palabras extraidas del libro
# word_list = process_file('mujeres.txt',skip_header=False)

# #genera un diccionario de listas con las variaciones de cada palabra
# diccionario = password_maker_p(word_list)




# key_list = diccionario.keys()

# print word_list

#imprime una lista de palabras 
# for key in sorted(key_list):
#     print key

#Imprime las contrasenas disponibles en la llave que se le expesifica
# print word_list

#Imprime una lista con las llaves de diccionario 
#key_print(keySorter(diccionario))


#Falta una funcion que imprima solo los valores del diccionario (una lista gigante)
#Una funcion que pruebe si una palabra esta en el diccionario y si no que la agrege
#Una funcion que reciba los parametros de una 


