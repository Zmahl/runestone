

from os import curdir


def insertion_sort(arr):

    #Consider the first "half" of the array sorted

    #Iterate over the entire array
    for i in range(1, len(arr)):

        #Set the current value equal to the ith element
        current = arr[i]

        #Set the comparison tracker to the ith element
        j = i

        #Loop through the sorted part of the array, comparing the current value to each one until the ith element will fit into the sorted list
        while j > 0 and arr[j - 1] > current:
            #Set the current
            arr[j] = arr[j - 1]
            j -= 1
        
        #Set the current value to the jth index in the sorted array
        arr[j] = current

arr = [12, 11, 13, 5, 6]
insertion_sort(arr)


for i in range(len(arr)):
    print("% d" % arr[i])
