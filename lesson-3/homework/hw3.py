Here are my answers: 

1) Create and Access List Elements
fruits = ["apple", "banana", "cherry", "grape", "mango"]
print(fruits[2])   # third fruit (index starts at 0)

2) Concatenate Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)

3) Extract Elements from a List
numbers = [10, 20, 30, 40, 50]

first = numbers[0]
middle = numbers[len(numbers)//2]   # middle element
last = numbers[-1]

new_list = [first, middle, last]
print(new_list)

4) Convert List to Tuple
movies = ["Inception", "Titanic", "Avatar", "Gladiator", "Interstellar"]
movies_tuple = tuple(movies)
print(movies_tuple)

5) Check Element in a List
cities = ["London", "Berlin", "Paris", "Rome"]
if "Paris" in cities:
    print("Paris is in the list")
else:
    print("Paris is not in the list")

6) Duplicate a List Without Using Loops
numbers = [1, 2, 3]
duplicate = numbers * 2
print(duplicate)

7) Swap First and Last Elements of a List
numbers = [10, 20, 30, 40, 50]

numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)

8) Slice a Tuple
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(nums[3:8])   # slice index 3 to 7

9) Count Occurrences in a List
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
print(colors.count("blue"))

10) Find the Index of an Element in a Tuple
animals = ("cat", "dog", "lion", "tiger", "elephant")
print(animals.index("lion"))

11) Merge Two Tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)
merged = t1 + t2
print(merged)

12) Find the Length of a List and Tuple
my_list = [10, 20, 30, 40]
my_tuple = (100, 200, 300)

print(len(my_list))
print(len(my_tuple))

13) Convert Tuple to List
nums = (5, 10, 15, 20, 25)
nums_list = list(nums)
print(nums_list)

14) Find Maximum and Minimum in a Tuple
numbers = (10, 3, 45, 7, 22)
print("Max:", max(numbers))
print("Min:", min(numbers))

15) Reverse a Tuple
words = ("Python", "is", "fun")
print(words[::-1])
