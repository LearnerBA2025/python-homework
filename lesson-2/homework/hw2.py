Here are my answers to the questions: 

1) Age Calculator (strings only)
name = input("Enter your name: ")
birth_year = input("Enter your birth year: ")

current_year = "2025"   # keep it as a string

# convert to integers by wrapping with int()
age = int(current_year) - int(birth_year)

print("Hello " + name + "! You are " + str(age) + " years old.")

2) Extract Car Names (txt = 'LMaasleitbtui')
txt = "LMaasleitbtui"

# Even index letters → Lasetti
car1 = txt[::2]

# Odd index letters → Malibu
car2 = txt[1::2]

print(car1)   # Lasetti
print(car2)   # Malibu

3) Extract Car Names (txt = 'MsaatmiazD')
txt = "MsaatmiazD"

# Even index letters → Matiz
car1 = txt[::2]

# Odd index letters → samaD (reverse to read properly)
car2 = txt[1::2][::-1]

print(car1)   # Matiz
print(car2)   # Damas

4) Extract Residence Area
txt = "I'am John. I am from London"

# Split text into parts
parts = txt.split("from")
area = parts[1].strip()

print(area)  # London

5) Reverse String
s = input("Enter a string: ")
print("Reversed: " + s[::-1])

6) Count Vowels
s = input("Enter text: ")
vowels = "aeiouAEIOU"
count = 0

for ch in s:
    if ch in vowels:
        count = count + 1

print("Number of vowels: " + str(count))

7) Find Maximum Value (simple strings only)

Since you don’t know lists yet, we can “fake” it by asking the user for three numbers and comparing them as strings converted to int.

a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")

# turn into integers
a = int(a)
b = int(b)
c = int(c)

# simple comparisons
max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c

print("Max value is " + str(max_val))

8) Check Palindrome
word = input("Enter a word: ")

# make both sides the same case
w = word.lower()

if w == w[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

9) Extract Email Domain
email = input("Enter your email: ")

parts = email.split("@")
domain = parts[1]

print("Domain: " + domain)

10) Generate Random Password

Since you haven’t covered random, we’ll make a fake password generator by simply reversing the name and adding digits — just using strings.

name = input("Enter your name: ")

# Make a simple "password" using string tricks
password = name[::-1] + "123!"

print("Your password could be: " + password)
