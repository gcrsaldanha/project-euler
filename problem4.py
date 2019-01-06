'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

UPPER_LIMIT = 999
LOWER_LIMIT = 100 - 1


# TODO: converting to integer and comparing is faster
def is_palindrome(number):
    return str(number)[::-1] == str(number)


def get_largest_palindrome():
    largest_palindrome = 0
    for a in range(UPPER_LIMIT, LOWER_LIMIT, -1):
        for b in range(a, LOWER_LIMIT, -1):  # since a * b == b * a.
            candidate = a * b
            if candidate <= largest_palindrome:
                break
            if is_palindrome(candidate):
                largest_palindrome = candidate
    return largest_palindrome


if __name__ == '__main__':
    print(get_largest_palindrome())
