"""
This script covers the second chapter in Grokking Algorithms
Alejandro Guillen
TEC - Electronics engineering
"""

"""
Summary on run times

          Arrays  Lists
Reading   O(1)    O(n)
Insertion O(n)    O(1)
Deletion  O(n)    O(1)



With an array all elements are stored right next to each other
With a list, elements are strewn all over the memory, each element stores the adress of the next one

Arrays allow faster reads
Linked lists are faster for inserts and deletes

All elements in an array must be the same type, a list doesn't care

"""
import random
#This chapter also covers selection sort, a not so fast algorithm

def findSmallest(arr): #This function find the position of the smallest value in the array
    smallest = arr[0]
    smallest_index = 0
    for i in range (len(arr)): #search through the array the smallest
        if arr[i] < smallest:
            smallest = arr[i] #if met update the smallest value
            smallest_index = i #if met update the index 
    return smallest_index

def selectionSort(arr): #this would be the 'main' function and sorts the array
    newArr = [] #in here we will build a new sorted array
    for i in range(len(arr)):
        smallest=findSmallest(arr) #here we call findSmallest
        print(smallest)
        newArr.append(arr.pop(smallest))#append the smallest value to the new array and pop out the value of "arr"
    return newArr
def randomarr(lenght): #This function 
    newarr = []
    for i in range(lenght):
        newarr.append(random.randint(0,100))
    print(newarr)
    return newarr

print(selectionSort(randomarr(10)))
