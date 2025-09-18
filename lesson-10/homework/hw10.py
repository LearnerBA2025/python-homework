Here are my answers: 

Homework 1: ToDo List CLI
from datetime import date

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"{self.title} ({self.due_date}) - {self.status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_all_tasks(self):
        for task in self.tasks:
            print(task)

    def list_incomplete_tasks(self):
        for task in self.tasks:
            if task.status == "Incomplete":
                print(task)


# CLI
todo = ToDoList()

while True:
    print("\n--- ToDo List Menu ---")
    print("1. Add Task")
    print("2. Mark Task Complete")
    print("3. List All Tasks")
    print("4. List Incomplete Tasks")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Task Title: ")
        desc = input("Description: ")
        y, m, d = map(int, input("Due date (YYYY MM DD): ").split())
        task = Task(title, desc, date(y, m, d))
        todo.add_task(task)
    elif choice == "2":
        todo.list_all_tasks()
        idx = int(input("Which task number to mark complete? ")) - 1
        if 0 <= idx < len(todo.tasks):
            todo.tasks[idx].mark_complete()
    elif choice == "3":
        todo.list_all_tasks()
    elif choice == "4":
        todo.list_incomplete_tasks()
    elif choice == "5":
        break
    else:
        print("❌ Invalid choice")

🔹 Homework 2: Blog System CLI
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        for i, post in enumerate(self.posts, start=1):
            print(f"{i}. {post}")

    def posts_by_author(self, author):
        for post in self.posts:
            if post.author == author:
                print(post)

    def delete_post(self, idx):
        if 0 <= idx < len(self.posts):
            self.posts.pop(idx)

    def edit_post(self, idx, new_content):
        if 0 <= idx < len(self.posts):
            self.posts[idx].content = new_content

    def latest_post(self):
        if self.posts:
            print("Latest:", self.posts[-1])
        else:
            print("No posts yet.")


# CLI
blog = Blog()

while True:
    print("\n--- Blog Menu ---")
    print("1. Add Post")
    print("2. List All Posts")
    print("3. Show Posts by Author")
    print("4. Edit Post")
    print("5. Delete Post")
    print("6. Show Latest Post")
    print("7. Exit")

    choice = input("Choose: ")

    if choice == "1":
        t = input("Title: ")
        c = input("Content: ")
        a = input("Author: ")
        blog.add_post(Post(t, c, a))
    elif choice == "2":
        blog.list_all_posts()
    elif choice == "3":
        a = input("Author name: ")
        blog.posts_by_author(a)
    elif choice == "4":
        blog.list_all_posts()
        idx = int(input("Post number to edit: ")) - 1
        new_c = input("New content: ")
        blog.edit_post(idx, new_c)
    elif choice == "5":
        blog.list_all_posts()
        idx = int(input("Post number to delete: ")) - 1
        blog.delete_post(idx)
    elif choice == "6":
        blog.latest_post()
    elif choice == "7":
        break
    else:
        print("❌ Invalid choice")

🔹 Homework 3: Banking System CLI
class Account:
    def __init__(self, acc_number, holder_name, balance=0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("❌ Insufficient funds!")

    def __str__(self):
        return f"{self.acc_number} | {self.holder_name} | Balance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.acc_number] = account

    def check_balance(self, acc_number):
        return self.accounts[acc_number].balance

    def transfer(self, from_acc, to_acc, amount):
        if self.accounts[from_acc].balance >= amount:
            self.accounts[from_acc].withdraw(amount)
            self.accounts[to_acc].deposit(amount)
        else:
            print("❌ Transfer failed: insufficient funds.")

    def display_account(self, acc_number):
        print(self.accounts[acc_number])


# CLI
bank = Bank()

while True:
    print("\n--- Banking Menu ---")
    print("1. Add Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transfer Money")
    print("6. Display Account")
    print("7. Exit")

    choice = input("Choose: ")

    if choice == "1":
        acc = input("Account Number: ")
        name = input("Holder Name: ")
        bal = float(input("Initial Balance: "))
        bank.add_account(Account(acc, name, bal))
    elif choice == "2":
        acc = input("Account Number: ")
        amt = float(input("Deposit Amount: "))
        bank.accounts[acc].deposit(amt)
    elif choice == "3":
        acc = input("Account Number: ")
        amt = float(input("Withdraw Amount: "))
        bank.accounts[acc].withdraw(amt)
    elif choice == "4":
        acc = input("Account Number: ")
        print("Balance:", bank.check_balance(acc))
    elif choice == "5":
        f = input("From Account: ")
        t = input("To Account: ")
        amt = float(input("Amount: "))
        bank.transfer(f, t, amt)
    elif choice == "6":
        acc = input("Account Number: ")
        bank.display_account(acc)
    elif choice == "7":
        break
    else:
        print("❌ Invalid choice")
