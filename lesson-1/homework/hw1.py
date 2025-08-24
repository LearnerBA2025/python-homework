Here are my answers to the questions: 

# 1. Given a side of square. Find its perimeter and area.

side = float(input("Enter the side of the square: "))
perimeter = 4 * side
area = side * side

print("Perimeter of square:", perimeter)
print("Area of square:", area)


# 2. Given diameter of circle. Find its length (circumference).

import math  # math library for pi

diameter = float(input("Enter the diameter of the circle: "))
circumference = math.pi * diameter   # formula = π * d

print("Circumference of circle:", circumference)


# 3. Given two numbers a and b. Find their mean.

a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))

mean = (a + b) / 2

print("Mean of a and b:", mean)


# 4. Given two numbers a and b. Find their sum, product and square of each number.

a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))

sum_ab = a + b
product_ab = a * b
square_a = a ** 2
square_b = b ** 2

print("Sum of a and b:", sum_ab)
print("Product of a and b:", product_ab)
print("Square of a:", square_a)
print("Square of b:", square_b)

