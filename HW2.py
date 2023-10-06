import random

#get the fibonacci numbers of input n
def fibonacci(n):
    a, b = 0, 1
    fib=[]
    while a<n:
        fib.append(a)
        a,b = b,a+b
    return fib

# the loop guarded command function
def lgc_function(range_start, range_end, x):
    # n is the amount of loop of bool expression
    n = range_end-range_start
    # define m to record the amount of true value of bool expression
    m=0
    # define result to record the integers in bool expression
    result=[]
    # run a loop of Boolean expressions from range_start to range_end
    for i in range(n+1):
        if x % range_start==0:
            m+=1
        result.append(range_start)
        range_start+=1

    # determine if bool expression get the true value in the loop
    # when m=0, it shows no bool expression get the true value,then throw runtime errors
    # when m>0, print out the Fibonacci numbers of integers randomly
    if m==0:
        raise RuntimeError("Invalid input: x does not satisfy any of the Boolean expressions.")
    else:
        r=int(random.choice(result))
        print(fibonacci(r))

if __name__ == "__main__":
    # enter the three integers the function needs
    range_start = int(input("Enter the first integer: "))
    range_end = int(input("Enter the second integer: "))
    x = int(input("Enter the third integer: "))

    try:
        lgc_function(range_start, range_end, x)
    except RuntimeError as e:
        print(e)
