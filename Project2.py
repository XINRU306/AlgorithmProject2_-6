import time
import math
import numpy as np
import random
# calculate the theoretical result of running time
def calculate():
    n = 1000000
    r = math.log(n)
    print(r)

# use the binary search method to find the largest element of sorted array
def find_largest_element(A):
    left = 0
    right = len(A) - 1

    while left < right:
        mid = (left + right+1) // 2
        if A[mid] > A[left] and A[mid] > A[right]:
            return A[mid]
        elif A[mid] > A[left]:
            left = mid
        else:
            right = mid - 1

    return A[left]  # or A[right]

def main():
    # initialize the n as the size of array
    n=1000
    A = np.arange(0, n, 1)
    # random initialize the k to circular shift the array
    k=random.randint(1,n)
    #Circular shift tp left by k positions
    np.roll(A,k)
    # Record the start time of the function
    start_time = time.time_ns()
    b=find_largest_element(A)
    print(b)
    # Record the end time of the function
    end_time = time.time_ns()
    result_time=end_time-start_time
    print('cost %f nanosecond'%result_time)

main()
calculate()