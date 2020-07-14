# # TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # initalize current index at 0
        cur_index = i
        # as we traverse through the index we set the smallest index to current index becuase
        # it is assumed elements before are already ordered
        smallest_index = cur_index
        
        # we need a second for loop to only check the indexes greater than the current index
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # when the nested loop finishes swap indexes of smallest index
        if smallest_index != i:
            # important to note order of swap order of operation
            arr[smallest_index], arr[i] = arr[i], arr[smallest_index]            
    return arr

test_arr = [4,7,22,2,8,9,11,1,3]
print(selection_sort(test_arr))

# # TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # lets initialize a local variable to False
    is_sorted = False

    while is_sorted == False:
        is_sorted = True
                
        for i in range(0, len(arr) - 1):
            left_value = arr[i]
            right_value = arr[i + 1]

            if left_value > right_value:
                is_sorted = False
                # here is where the swapping happens
                arr[i] = right_value
                arr[i+1] = left_value

    return arr

def bubble_sort_2(arr):
    # a condenced version of the above bubble sort
    # lets initialize a local variable to False
    is_sorted = False

    while is_sorted == False:
        is_sorted = True
       
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                is_sorted = False
                # here is where the swapping happens
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


print(bubble_sort_2(test_arr))
test_arr[0] = 99
test_arr[0 + 1] = 88
print(test_arr) 
# '''
# STRETCH: implement the Counting Sort function below

# Counting sort is a sorting algorithm that works on a set of data where
# we specifically know the maximum value that can exist in that set of
# data. The idea behind this algorithm then is that we can create "buckets"
# from 0 up to the max value. This is most easily done by initializing an
# array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

# Each buckets[i] then is responsible for keeping track of how many times 
# we've seen `i` in the input set of data as we iterate through it.
# Once we know exactly how many times each piece of data in the input set
# showed up, we can construct a sorted set of the input data from the 
# buckets. 

# What is the time and space complexity of the counting sort algorithm?
# '''
# def counting_sort(arr, maximum=None):
#     # Your code here


#     return arr
