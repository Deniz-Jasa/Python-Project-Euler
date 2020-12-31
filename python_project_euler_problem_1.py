# Python Project Euler - Problem 1 - Deniz Jasarbasic

# Question: If we list all the natural numbers below 10 that are multiples of 
# 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum 
# of all the multiples of 3 or 5 below 1000.

# Solution:

sum_multiple = 0

def is_multiple (n):
    return (n%5 == 0 or n%3 == 0)

for i in range(1000):
    if is_multiple(i):
        sum_multiple += i

print(sum_multiple)