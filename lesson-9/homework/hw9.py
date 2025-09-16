Here are my answers: 
OOP Homework Solutions
1. Circle Class
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# Test
c = Circle(5)
print("Circle area:", c.area())         # 78.54
print("Circle perimeter:", c.perimeter())  # 31.41

2. Person Class
from datetime import date

class Person:
    def __init__(self, name, country, birthdate):
        self.name = name
        self.country = country
        self.birthdate = birthdate  # (YYYY, M, D) tuple

    def age(self):
        today = date.today()
        birth = date(*self.birthdate)
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

# Test
p = Person("Ali", "Uzbekistan", (2000, 5, 14))
print("Name:", p.name)
print("Age:", p.age())

3. Calculator Class
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

# Test
calc = Calculator()
print(calc.add(5, 3))       # 8
print(calc.divide(10, 0))   # Error

4. Shape and Subclasses
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# Test
shapes = [Circle(5), Square(4), Triangle(3, 4, 5)]
for s in shapes:
    print(type(s).__name__, "Area:", s.area(), "Perimeter:", s.perimeter())

5. Binary Search Tree Class
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.key:
            if root.left:
                self._insert(root.left, key)
            else:
                root.left = Node(key)
        elif key > root.key:
            if root.right:
                self._insert(root.right, key)
            else:
                root.right = Node(key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if not root:
            return False
        if key == root.key:
            return True
        elif key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)

# Test
tree = BST()
for val in [10, 5, 20, 3, 7]:
    tree.insert(val)

print(tree.search(7))   # True
print(tree.search(15))  # False

6. Stack Data Structure
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return "Stack is empty"
        return self.items.pop()

# Test
s = Stack()
s.push(1)
s.push(2)
print(s.pop())  # 2
print(s.pop())  # 1
print(s.pop())  # Stack is empty

7. Linked List Data Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Test
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()   # 30 -> 20 -> 10 -> None
ll.delete(20)
ll.display()   # 30 -> 10 -> None

8. Shopping Cart Class
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = self.items.get(item, 0) + price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total(self):
        return sum(self.items.values())

# Test
cart = ShoppingCart()
cart.add_item("Apple", 2)
cart.add_item("Banana", 1)
print("Total:", cart.total())  # 3
cart.remove_item("Banana")
print("Total:", cart.total())  # 2

9. Stack with Display
class StackWithDisplay:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack.pop()

    def display(self):
        print("Stack:", self.stack)

# Test
st = StackWithDisplay()
st.push(5)
st.push(10)
st.display()   # [5, 10]
print(st.pop())  # 10

10. Queue Data Structure
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            return "Queue is empty"
        return self.queue.pop(0)

# Test
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # 1
print(q.dequeue())  # 2
print(q.dequeue())  # Queue is empty

11. Bank Class
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"{self.name} withdrew {amount}. New balance: {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, name, balance=0):
        self.accounts[name] = BankAccount(name, balance)

    def get_account(self, name):
        return self.accounts.get(name, None)

# Test
bank = Bank()
bank.add_account("Ali", 100)
acc = bank.get_account("Ali")
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(200)
