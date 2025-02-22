import time
import random

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

def sequential_search(a_list, item):
    start_time = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    end_time = time.time()

    #returns found variable and the total time taken for function and returns a sorted list
    return found, (end_time - start_time)


def ordered_sequential_search(a_list, item):
    start_time = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    end_time = time.time()
    
    #returns found variable and the total time taken for function and returns a sorted list
    return found, (end_time - start_time)


def binary_search_iterative(a_list,item):
    start_time = time.time()
    first = 0
    
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end_time = time.time()
    
    #returns found variable and the total time taken for function and returns a sorted list
    return found, (end_time - start_time)
    

def binary_search_recursive(a_list, item):
    start_time = time.time()
    
    def binary_search(a_list, item):
        if len(a_list) == 0:
            return False
        else:
            midpoint = len(a_list) // 2
            if a_list[midpoint] == item:
                return True
            else:
                if item < a_list[midpoint]:
                    return binary_search(a_list[:midpoint], item)
                else:
                    return binary_search(a_list[midpoint + 1:], item)
    
    found = binary_search(a_list, item)
    end_time = time.time()

    #returns found variable and the total time taken for function and returns a sorted list
    return found, (end_time - start_time)

if __name__ == "__main__":
    #initialize list sizes 
    list_sizes = [500, 1000, 5000]

    #for each list size
    for size in list_sizes:
        seq_search_total_time = 0
        ord_seq_search_total_time = 0
        bin_search_itr_total_time = 0
        bin_search_rec_total_time = 0

        #generate 100 lists 
        for i in range(100):
            mylist = get_me_random_list(size)
            sorted_mylist = sorted(mylist)
            
            #aggregates the time taken for each function
            seq_search_total_time += sequential_search(mylist, 99999999)[1]
            ord_seq_search_total_time += ordered_sequential_search(sorted_mylist, 99999999)[1]
            bin_search_itr_total_time += binary_search_iterative(sorted_mylist, 99999999)[1]
            bin_search_rec_total_time += binary_search_recursive(sorted_mylist, 99999999)[1]

        #prints the average time for the functions based on list size
        print(f"Sequential Search took {seq_search_total_time/100:10.7f} seconds to run, on average for a list of {size} elements")
        print(f"Ordered Sequential Search took {ord_seq_search_total_time/100:10.7f} seconds to run, on average for a list of {size} elements")
        print(f"Binary Search Iterative took {bin_search_itr_total_time/100:10.7f} seconds to run, on average for a list of {size} elements")
        print(f"Binary Search Recursive took {bin_search_rec_total_time/100:10.7f} seconds to run, on average for a list of {size} elements")
        print()
