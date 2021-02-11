# Python Project Euler - Problem 20 - Deniz Jasarbasic

# Solution:

def compute_factorial(n):

    if n < 1:
        return 1
    else:
        return_number = n * compute_factorial(n-1)
        return return_number

def compute_sum(n):
    factorial_sum = sum(int(c) for c in str(compute_factorial(n)))
    return str(factorial_sum)

print(compute_sum(100))