Here are my answers to the questions: 

Dictionary Exercises
1) Sort a Dictionary by Value
my_dict = {1: 2, 3: 1, 2: 4}

# Sort ascending by value
asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print("Ascending:", asc)

# Sort descending by value
desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print("Descending:", desc)

2) Add a Key to a Dictionary
d = {0: 10, 1: 20}
d[2] = 30   # add new key:value
print(d)    # {0: 10, 1: 20, 2: 30}

3) Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = {}
for d in (dic1, dic2, dic3):
    result.update(d)

print(result)
# {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}

4) Generate a Dictionary with Squares
n = 5
squares = {}
for x in range(1, n+1):
    squares[x] = x * x

print(squares)
# {1:1, 2:4, 3:9, 4:16, 5:25}

5) Dictionary of Squares (1 to 15)
squares = {}
for x in range(1, 16):
    squares[x] = x * x

print(squares)

Set Exercises
1) Create a Set
my_set = {1, 2, 3}
print(my_set)

2) Iterate Over a Set
my_set = {"apple", "banana", "cherry"}

for item in my_set:
    print(item)

3) Add Member(s) to a Set
my_set = {1, 2, 3}
my_set.add(4)          # add one item
my_set.update([5, 6])  # add multiple items
print(my_set)

4) Remove Item(s) from a Set
my_set = {1, 2, 3, 4}
my_set.remove(3)   # remove 3
print(my_set)

5) Remove an Item if Present in the Set
my_set = {1, 2, 3}
my_set.discard(2)   # remove safely if exists
my_set.discard(5)   # does nothing if 5 not in set
print(my_set)
