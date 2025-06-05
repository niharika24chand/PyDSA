#calculate the fibonacci number present at position n (using dynamic programming)
def fibo(n,result = {}):
    if n <= 1:
        return n
    if n not in result:
            result[n] = fibo(n-1, result) + fibo(n-2, result)
    return result[n]

print("Fibonacci series: ", fibo(15))


