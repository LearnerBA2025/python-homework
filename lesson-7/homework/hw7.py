Here are my answers: 

Homework on Python Functions
Theory Part (map and filter with examples)
map()

map(function, iterable) applies a function to every element of an iterable (like list).

Returns a map object (iterator), which can be converted to a list.

Example with lambda:

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

filter()

filter(function, iterable) keeps only the elements that make the function return True.

Returns a filter object (iterator).

Example with lambda:

numbers = [10, 15, 20, 25, 30]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [10, 20, 30]

🔹 Problem Solutions
1. is_prime(n)

Checks whether a number is prime.

def is_prime(n: int) -> bool:
    """Check if n is a prime number (n > 0)."""
    if n < 2:  # 0 and 1 are not prime
        return False
    for i in range(2, int(n**0.5) + 1):  # check divisors up to sqrt(n)
        if n % i == 0:
            return False
    return True

# Test cases
print(is_prime(4))  # False
print(is_prime(7))  # True
print(is_prime(1))  # False

Explanation:

We loop only up to sqrt(n) (optimization).

If divisible by any number (except 1 and itself), return False.

2. digit_sum(k)

Calculates the sum of digits of k.

def digit_sum(k: int) -> int:
    """Return the sum of digits of integer k."""
    return sum(int(digit) for digit in str(k))

# Test cases
print(digit_sum(24))   # 6 → 2 + 4
print(digit_sum(502))  # 7 → 5 + 0 + 2
print(digit_sum(1234)) # 10 → 1 + 2 + 3 + 4


Explanation:

Convert number to string → iterate digits → convert back to int → sum them.

3. Powers of Two ≤ N
def powers_of_two(N: int):
    """Print all powers of 2 that are ≤ N."""
    k = 1
    while 2**k <= N:
        print(2**k, end=" ")
        k += 1
    print()  # new line after output

# Test cases
powers_of_two(10)   # 2 4 8
powers_of_two(30)   # 2 4 8 16
powers_of_two(1)    # (prints nothing)


Explanation:

Start with 2**1 = 2.

Keep going while result ≤ N.

Print results on the same line.


