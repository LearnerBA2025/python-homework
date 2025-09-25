Here are my homework answers: 

import re
from datetime import datetime, timedelta
import time
import pytz   # you might need to install: pip install pytz

----------------- Exercise 1: Age Calculator -----------------
def age_calculator():
    birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d").date()
    today = datetime.today().date()

    # Calculate years, months, days
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        last_month = (today.month - 1) if today.month > 1 else 12
        last_year = today.year if today.month > 1 else today.year - 1
        days += (datetime(last_year, last_month % 12 + 1, 1) - timedelta(days=1)).day

    if months < 0:
        years -= 1
        months += 12

    print(f"You are {years} years, {months} months, and {days} days old.")

----------------- Exercise 2: Days Until Next Birthday -----------------
def days_until_birthday():
    birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d").date()
    today = datetime.today().date()

    next_birthday = birthdate.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    delta = next_birthday - today
    print(f"Days until your next birthday: {delta.days}")

----------------- Exercise 3: Meeting Scheduler -----------------
def meeting_scheduler():
    current_str = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
    duration_str = input("Enter meeting duration (hours minutes): ")

    current_dt = datetime.strptime(current_str, "%Y-%m-%d %H:%M")
    hours, minutes = map(int, duration_str.split())
    end_dt = current_dt + timedelta(hours=hours, minutes=minutes)

    print(f"Meeting will end at: {end_dt.strftime('%Y-%m-%d %H:%M')}")

----------------- Exercise 4: Timezone Converter -----------------
def timezone_converter():
    date_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
    from_tz = input("Enter your current timezone (e.g., Asia/Tashkent): ")
    to_tz = input("Enter the target timezone (e.g., US/Eastern): ")

    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)

    local_dt = from_zone.localize(dt)
    converted = local_dt.astimezone(to_zone)

    print("Converted datetime:", converted.strftime("%Y-%m-%d %H:%M %Z%z"))

----------------- Exercise 5: Countdown Timer -----------------
def countdown_timer():
    future_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
    future_dt = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

    while True:
        now = datetime.now()
        if now >= future_dt:
            print("Time is up!")
            break
        delta = future_dt - now
        print(f"Time remaining: {delta}")
        time.sleep(1)

----------------- Exercise 6: Email Validator -----------------
def email_validator():
    email = input("Enter an email: ")
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        print("Valid email address.")
    else:
        print("Invalid email address.")

----------------- Exercise 7: Phone Number Formatter -----------------
def phone_formatter():
    number = input("Enter a 10-digit phone number: ")
    digits = re.sub(r"\D", "", number)
    if len(digits) == 10:
        formatted = f"({digits[0:3]}) {digits[3:6]}-{digits[6:]}"
        print("Formatted phone number:", formatted)
    else:
        print("Invalid phone number.")

----------------- Exercise 8: Password Strength Checker -----------------
def password_checker():
    pwd = input("Enter a password: ")
    length_ok = len(pwd) >= 8
    has_upper = re.search(r"[A-Z]", pwd)
    has_lower = re.search(r"[a-z]", pwd)
    has_digit = re.search(r"\d", pwd)

    if length_ok and has_upper and has_lower and has_digit:
        print("Strong password.")
    else:
        print("Weak password. Must be 8+ chars, include uppercase, lowercase, and digit.")

----------------- Exercise 9: Word Finder -----------------
def word_finder():
    text = """Python is a powerful language. Python can be used for web development,
    data analysis, and more. Learning Python is fun!"""
    word = input("Enter a word to search: ")
    matches = [m.start() for m in re.finditer(word, text, re.IGNORECASE)]
    if matches:
        print(f"Word '{word}' found at positions:", matches)
    else:
        print(f"Word '{word}' not found.")

----------------- Exercise 10: Date Extractor -----------------
def date_extractor():
    text = input("Enter text containing dates: ")
    pattern = r"\b\d{4}-\d{2}-\d{2}\b"  # matches YYYY-MM-DD
    dates = re.findall(pattern, text)
    if dates:
        print("Dates found:", dates)
    else:
        print("No dates found.")
