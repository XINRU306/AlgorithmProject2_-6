import time
import math
import numpy as np

def caulate():
    n=1000000000
    r=pow(n,(2/3))
    print(r)

def test():
    n=1000000000
    Sum=0
    a=np.random.randint(0, 100, size=n)
    b=np.random.randint(0, 100, size=n)
    start_time = time.time_ns()  # Record the start time of the function
    j=2
    while j<n:
        k=j
        while k<n:
            Sum += a[k]*b[k]
            k += int(pow(n,(1/3))*math.log(n,2))
        j=j*2

    end_time = time.time_ns()  # Record the end time of the function
    print('cost %f nanosecond' % (end_time - start_time))

test()
caulate()






