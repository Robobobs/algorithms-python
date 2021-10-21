def fact(n):
    '''factorial function that assumes n is a positive integer greater than or equal to 1'''
    if n >= 1:
        return n * fact(n-1)
    else:
        return 1

def fib(n):
    '''fibernaci function that assumed n is a positive integer greater than 0'''
    if n >= 3:
        return fib(n-1) + fib(n-2)
    else:
        return 1




# ------------------------------- TEST CASE --------------------------------- #

print(fact(1)) # 1! should return 1
print(fact(5)) # 5! should return 120

print(fib(1)) # should return 1
print(fib(6)) # should return 8

'''
# --------------------------------- NOTES ----------------------------------- #

When a recursive function calls itself, this is known as a 'recursive case'. When
it return 1, this is known as the 'base case'.


'''
