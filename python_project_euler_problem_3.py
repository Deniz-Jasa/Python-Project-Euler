# Python Project Euler - Problem 3 - Deniz Jasarbasic

# Question: The prime factors of 13195 are 5, 7, 13 and 29. 
# What is the largest prime factor of the number 600851475143 ?

# Solution:

def largest_prime_factor(num):
    
    prime_factor = 1
    i = 2

    while (i <= num/i):
        if (num%i == 0):
            prime_factor = i
            num /= i
        else:
            i += 1

        if (prime_factor < num):
            prime_factor = num

    return prime_factor

print(largest_prime_factor(600851475143))