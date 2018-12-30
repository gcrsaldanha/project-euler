import math

from decorators import timing

'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
'''
13195 = 5 * 7 * 13 * 29
600851475143 = f1 * f2 * f3 ... * fn
Problem: find the largest prime factor of a given number
- How to find a prime factor?
    - Must be prime
    - Must be a factor
- Smaller prime factor: 2

# Plan 1
- Divide N by i where i goes from 1 up to N/2, for every i where N % i == 0, add i to divisors list
- Filter divisors list for prime numbers (factors)
- Get the last number => largest prime factor
=> Impossible! Too long!

## Improvements
- I know it does not have 2 as a factor since it's not an *even* number
- I know it does not have 3 as a factor since it's not divisible by 3
=> i may go only up to X where X is N/(largest_non_divisor)
    i.e., for every step, I can divide N/i
'''


def range_end(start, end, step=1):
    return range(start, end+1, step)

# @timing
# def is_prime(number):
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True


# @timing
# def is_prime(number):
#     for i in range(2, number//2):
#         if number % i == 0:
#             return False
#     return True


# @timing
def is_prime(number):
    for i in range_end(2, int(math.sqrt(number))):  # must be inclusive end
        if number % i == 0:
            return False
    return True


# @timing
# def get_largest_prime(number):
#     divisors = [
#         divisor for divisor in range_end(1, number)
#         if number % divisor == 0 and is_prime(divisor)
#     ]
#     return divisors[-1]

# TEST: if the given number is the largest factor itself, range(1, number) X
# TODO: compute algorithm complexity

# 13195 = 5, 7, 13, 29
@timing
def get_largest_prime(number):
    divisor = 1
    prime_factors = []
    i = 1
    while(i <= number // divisor):
        if number % i == 0:
            divisor = i
            if is_prime(divisor):
                prime_factors.append(divisor)
        i += 1
    return prime_factors[-1]


if __name__ == '__main__':
    number = 600851475143
    # number = 6008514  # 1 second! + 5 digits ~= 100000 seconds ~= 28 hours!
    # number = 13195
    largest_prime = get_largest_prime(number)
    # print(get_largest_prime.__name__) => without functools.wrap = time_func
    print('Largest prime: ', largest_prime)
