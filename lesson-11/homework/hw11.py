Here are my answers: 

Step 1: Create Virtual Environment & Install Packages

Open terminal (PowerShell / CMD / Bash):

# Create virtual environment (name: venv)
python -m venv venv

# Activate it

# On Windows:
venv\Scripts\activate


# Install some packages (example: requests, numpy)
pip install requests numpy

Step 2: Create Custom Modules

📂 Project Structure (so far)
project/
│── math_operations.py
│── string_utils.py

math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

string_utils.py
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

Step 3: Create Custom Packages
Geometry Package

Structure:

geometry/
│── __init__.py
│── circle.py

circle.py
import math

def calculate_area(radius):
    return math.pi * radius * radius

def calculate_circumference(radius):
    return 2 * math.pi * radius


(__init__.py can be empty or used to expose functions.)

File Operations Package

Structure:

file_operations/
│── __init__.py
│── file_reader.py
│── file_writer.py

file_reader.py
def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read()

file_writer.py
def write_file(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)

Step 4: Test Everything

Create main.py at root:

from math_operations import add, divide
from string_utils import reverse_string, count_vowels
from geometry.circle import calculate_area, calculate_circumference
from file_operations.file_reader import read_file
from file_operations.file_writer import write_file

# Math
print("Add:", add(10, 5))
print("Divide:", divide(10, 2))

# Strings
print("Reverse:", reverse_string("Python"))
print("Vowels:", count_vowels("Hello World"))

# Geometry
print("Area of circle (r=5):", calculate_area(5))
print("Circumference (r=5):", calculate_circumference(5))

# File operations
write_file("test.txt", "Hello from Python!")
print("File content:", read_file("test.txt"))


Run it:

python main.py
