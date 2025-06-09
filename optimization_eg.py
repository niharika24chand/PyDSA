# example on how to optimize a code (Eg: fibonacci)
import time

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]

start_time = time.time()
print("Before optimization: ")
print(f"Fibonacci of 30: {fib(30)}")
print(f"Time taken: {time.time() - start_time:.4f} seconds")

start_time = time.time()
print("After optimization: ")
print(f"Fibonacci of 30: {fib(30)}")
print(f"Time taken: {time.time() - start_time:.4f} seconds")