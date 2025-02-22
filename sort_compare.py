import argparse
# other imports go here

import random
import time

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list
    

def insertion_sort(a_list):
    
    start_time = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
    end_time = time.time()
    #returns total time taken for function
    return (end_time - start_time)


def shell_sort(alist):
    start_time = time.time()
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)

        #print("After increments of size", sublistcount, "The list is",alist)

        sublistcount = sublistcount // 2
    end_time = time.time()
    #returns total time taken for function
    return (end_time - start_time)
    


def python_sort(a_list):
    start_time = time.time()
    """
    Use Python built-in sorted function

    :param a_list:
    :return: the sorted list
    """
    a = sorted(a_list)
    end_time = time.time()
    #returns total time taken for function and returns a sorted list
    return a, (end_time - start_time)



def gapInsertionSort(alist, start, gap):

    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue


if __name__ == "__main__":
    #initialize list sizes 
    list_sizes = [500, 1000, 5000]

    #for each list size
    for size in list_sizes:
        insertion_sort_total_time = 0
        shell_sort_total_time = 0
        python_sort_total_time = 0

        #generate 100 lists 
        for i in range(100):
            mylist = get_me_random_list(size)

            #aggregates the time taken for each function 
            insertion_sort_total_time += insertion_sort(mylist)
            shell_sort_total_time += shell_sort(mylist)
            python_sort_time = python_sort(mylist)[1]
            python_sort_total_time += python_sort_time

        #prints the average time for the functions based on list size
        print(f"Insertion Sort took {insertion_sort_total_time/100:10.7f} seconds on average for list size of {size}")
        print(f"Shell Sort took {shell_sort_total_time/100:10.7f} seconds on average for list size of {size}")
        print(f"Python Sort took {python_sort_total_time/100:10.7f} seconds on average for list size of {size}")
        print()

        

        


  
