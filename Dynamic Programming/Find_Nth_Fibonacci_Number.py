#Recursive
def Fibonacci(n): 
    if n<=1: 
        return n
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2)

#Dynamic Programming - Memoization
def fib(n, lookup): 
  
    # Base case 
    if n == 0 or n == 1 : 
        lookup[n] = n 
  
    # If the value is not calculated previously then calculate it 
    if lookup[n] is None: 
        lookup[n] = fib(n-1 , lookup)  + fib(n-2 , lookup)  
  
    # return the value corresponding to that value of n 
    return lookup[n]