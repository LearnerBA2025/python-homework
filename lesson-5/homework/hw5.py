Here are my answers to the questions: 

 1) Leap year function

def is_leap(year):
    # A leap year must be divisible by 4
    # But if it is also divisible by 100, then it must also be divisible by 400
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Example tests
print(is_leap(1990))  # False
print(is_leap(2000))  # True
print(is_leap(1900))  # False
print(is_leap(2024))  # True

Other solution(option 2):
try:
    year = int(input("Enter a year to check if it is a leap year: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")

except ValueError:
    print("Year must be an integer.")


2) Conditional Statements (“Weird” problem)
n = int(input("Enter a number: "))

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and n >= 2 and n <= 5:
    print("Not Weird")
elif n % 2 == 0 and n >= 6 and n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

Other shorter solution(option 2):

n = int(input("Enter a number: "))
print(
    "Weird" if n % 2 == 1 or (6 <= n <= 20) else "Not Weird"
)


3) Even numbers between a and b (inclusive) without loop
Solution 1 (with if-else)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a % 2 == 0:
    start = a
else:
    start = a + 1

# range creates the even numbers without using a loop manually
evens = list(range(start, b + 1, 2))
print(evens)

Solution 2 (without if-else)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# If a is odd, add 1; if even, add 0
start = a + (a % 2)

evens = list(range(start, b + 1, 2))
print(evens)

