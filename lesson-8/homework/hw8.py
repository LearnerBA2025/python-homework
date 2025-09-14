Here are my answers: 

Python Exception Handling Homework Solutions
1. Handle ZeroDivisionError
try:
    a = 10
    b = 0
    result = a / b
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

2. Raise ValueError if input is not integer
try:
    num = input("Enter an integer: ")
    num = int(num)  # Raises ValueError if not integer
    print("You entered:", num)
except ValueError:
    print("Error: That is not a valid integer.")

3. Handle FileNotFoundError
try:
    with open("nonexistent.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File does not exist.")

4. Raise TypeError if inputs are not numerical
try:
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    if not (x.replace('.', '', 1).isdigit() and y.replace('.', '', 1).isdigit()):
        raise TypeError("Inputs must be numbers.")
    print("Sum =", float(x) + float(y))
except TypeError as e:
    print("Error:", e)

5. Handle PermissionError
try:
    with open("/root/secret.txt", "r") as f:
        print(f.read())
except PermissionError:
    print("Error: Permission denied to access the file.")

6. Handle IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # invalid index
except IndexError:
    print("Error: List index out of range.")

7. Handle KeyboardInterrupt
try:
    num = input("Enter a number (Ctrl+C to cancel): ")
    print("You entered:", num)
except KeyboardInterrupt:
    print("\nInput cancelled by user.")

8. Handle ArithmeticError
try:
    result = 10 / 0
except ArithmeticError:
    print("Error: Arithmetic operation failed.")

9. Handle UnicodeDecodeError
try:
    with open("test.txt", "r", encoding="ascii") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Error: Encoding issue while reading the file.")

10. Handle AttributeError
try:
    my_list = [1, 2, 3]
    my_list.upper()  # lists don’t have .upper()
except AttributeError:
    print("Error: Attribute not found for object.")

Python File I/O Homework Solutions
1. Read entire text file
with open("sample.txt", "r") as f:
    print(f.read())

2. Read first n lines
def read_first_n_lines(filename, n):
    with open(filename, "r") as f:
        for _ in range(n):
            print(f.readline(), end="")

read_first_n_lines("sample.txt", 3)

3. Append text and display
with open("sample.txt", "a") as f:
    f.write("\nAppended line.")

with open("sample.txt", "r") as f:
    print(f.read())

4. Read last n lines
def read_last_n_lines(filename, n):
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines[-n:]:
            print(line, end="")

read_last_n_lines("sample.txt", 2)

5. Read file line by line into a list
with open("sample.txt", "r") as f:
    lines = f.readlines()

print(lines)

6. Read file into a variable
with open("sample.txt", "r") as f:
    content = f.read()

print(content)

7. Read file into an array
with open("sample.txt", "r") as f:
    arr = [line.strip() for line in f]

print(arr)

8. Find longest words
with open("sample.txt", "r") as f:
    words = f.read().split()
    longest = max(words, key=len)
    print("Longest word:", longest)

9. Count number of lines
with open("sample.txt", "r") as f:
    print("Line count:", len(f.readlines()))

10. Count word frequency
from collections import Counter

with open("sample.txt", "r") as f:
    words = f.read().replace(",", " ").split()
    freq = Counter(words)

print(freq)

11. Get file size
import os
print("File size:", os.path.getsize("sample.txt"), "bytes")

12. Write list to file
my_list = ["apple", "banana", "cherry"]

with open("output.txt", "w") as f:
    for item in my_list:
        f.write(item + "\n")

13. Copy contents to another file
with open("sample.txt", "r") as f1, open("copy.txt", "w") as f2:
    f2.write(f1.read())

14. Combine lines from two files
with open("file1.txt") as f1, open("file2.txt") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())

15. Read a random line
import random

with open("sample.txt", "r") as f:
    lines = f.readlines()
    print("Random line:", random.choice(lines).strip())

16. Check if file is closed
f = open("sample.txt", "r")
print("File closed?", f.closed)
f.close()
print("File closed?", f.closed)

17. Remove newline characters
with open("sample.txt", "r") as f:
    lines = [line.strip() for line in f]

print(lines)

18. Count words in file
with open("sample.txt", "r") as f:
    words = f.read().replace(",", " ").split()
    print("Word count:", len(words))

19. Extract characters into list
chars = []
with open("sample.txt", "r") as f:
    for line in f:
        chars.extend(list(line.strip()))

print(chars)

20. Generate 26 files A.txt–Z.txt
import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}.txt")

21. Create file with alphabet letters (N per line)
import string

def write_alphabet_per_line(filename, n):
    letters = string.ascii_uppercase
    with open(filename, "w") as f:
        for i in range(0, len(letters), n):
            f.write(" ".join(letters[i:i+n]) + "\n")

write_alphabet_per_line("alphabet.txt", 5)
