Here are my answers to the questions:

1. Modify String with Underscores
def add_underscores(txt):
    result = ""
    count = 0
    vowels = "aeiou"

    for char in txt:
        result += char
        count += 1

        # every 3 characters, maybe add underscore
        if count == 3:
            if char.lower() not in vowels:   # skip underscore if vowel
                result += "_"
            count = 0  # reset counter

    return result

# Examples
print(add_underscores("hello"))    # hel_lo
print(add_underscores("assalom"))  # ass_alo_m
print(add_underscores("abcdefg"))  # abc_def_g

2. Integer Squares Exercise
n = int(input("Enter n: "))

for i in range(n):
    print(i ** 2)


3. Loop-Based Exercises
Exercise 1: First 10 natural numbers
i = 1
while i <= 10:
    print(i)
    i += 1

Exercise 2: Pattern
for i in range(1, 6):  # rows
    for j in range(1, i + 1):  # numbers in each row
        print(j, end=" ")
    print()

Exercise 3: Sum of numbers
num = int(input("Enter number: "))
total = 0
for i in range(1, num + 1):
    total += i
print("Sum is:", total)

Exercise 4: Multiplication table
n = int(input("Enter number: "))
for i in range(1, 11):
    print(n * i)

Exercise 5: Display numbers from list
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num % 5 == 0 and 70 < num <= 150:
        print(num)

Exercise 6: Count digits
num = int(input("Enter number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print("Total digits:", count)

Exercise 7: Reverse number pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

Exercise 8: Print list in reverse
list1 = [10, 20, 30, 40, 50]
for i in range(len(list1) - 1, -1, -1):
    print(list1[i])

Exercise 9: Numbers -10 to -1
for i in range(-10, 0):
    print(i)

Exercise 10: Done message
for i in range(5):
    print(i)
print("Done!")

Exercise 11: Prime numbers in a range
start = 25
end = 50

print("Prime numbers between", start, "and", end, ":")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

Exercise 12: Fibonacci series (10 terms)
n1, n2 = 0, 1
print("Fibonacci sequence:")
for _ in range(10):
    print(n1, end=" ")
    n1, n2 = n2, n1 + n2

Exercise 13: Factorial
num = int(input("Enter number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"{num}! =", fact)

4. Return Uncommon Elements of Lists
def uncommon_elements(list1, list2):
    result = []
    for x in list1:
        if x not in list2:
            result.append(x)
    for y in list2:
        if y not in list1:
            result.append(y)
    return result


# Tests
print(uncommon_elements([1, 1, 2], [2, 3, 4]))          # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))          # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]
