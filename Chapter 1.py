"""
These are the exercises explained in the first chapter of the book Grokking Algorithms
Alejandro Guillen Vargas
TEC - Electronics Engineering
"""
import random

def binary_search(lista, item):  #Main function, Algorithm binary search
    low = 0
    high = len(lista)-1
    while low <= high:
        mid = int((low+high)/2)
        guess = lista[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid +1
    return None




def createList(lenght):     #secondary function, Creates a "random" orginized list
    multiplier = random.randint(1,10)
    print("Multiplier  ",multiplier)
    offset = random.randint(1,15)
    lista = []
    i = 0
    while i < lenght:
        number = multiplier * i + offset
        lista.append(number)
        i= i+1
    print(lista)
    return lista
    
print(binary_search(createList(25), 46))
