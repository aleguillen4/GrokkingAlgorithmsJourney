"""
These are the exercises explained in the third chapter of the book Grokking Algorithms
Alejandro Guillen Vargas
TEC - Electronics Engineering
"""
"""
Chapter 3 is about recursion

"""
#This function search for a key in a box that contains boxes with boxes


def look_for_a_key(box):
    for itme in box:
        if item.is_a_box(): #recursive case
            look_for_a_key(item)
        elif item.is_a_key(): #base case
            print("Found the key!")

def factorial(x):
    print(x)
    if x==1: # base case
        return x
    else:   #recursive case
        return x * factorial(x-1)
print(factorial(5))
