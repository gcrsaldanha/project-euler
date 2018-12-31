import math

from decorators import timing

'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''


def range_end(start, end, step=1):
    '''Returns range with inclusive end'''
    return range(start, end+1, step)


# @timing
def is_prime(number):
    '''Returns True if number is prime. False otherwise'''
    for i in range_end(2, int(math.sqrt(number))):
        if number % i == 0:
            return False
    return True


@timing
def get_largest_prime_factor(number):
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
    # number = 13195
    number = 600851475143
    largest_prime = get_largest_prime_factor(number)
    print('Largest prime: ', largest_prime)


# TODO
# TEST: if the given number is the largest factor itself, range(1, number) X
