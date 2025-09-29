Here are my answers: 

Task 1: JSON Parsing (students.json)
import json

# Task 1: Read and print details of students
with open("students.json", "r", encoding="utf-8") as f:
    data = json.load(f)   # load JSON into Python

# Assume the file contains a list of students
for student in data:
    print("ID:", student.get("id"))
    print("Name:", student.get("name"))
    print("Age:", student.get("age"))
    print("Email:", student.get("email"))
    print("Courses:", student.get("courses"))
    print("-" * 30)


This reads a students.json file and prints each student’s info.

Task 2: Weather API (OpenWeatherMap)
import requests
import json

# Replace with your API key from https://openweathermap.org/
API_KEY = "YOUR_API_KEY"
CITY = "Tashkent"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()   # parse JSON response

if response.status_code == 200:
    print("City:", data["name"])
    print("Country:", data["sys"]["country"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])
else:
    print("Error:", data.get("message", "Unable to fetch weather"))


This fetches live weather for Tashkent.


Task 3: JSON Modification (books.json)
import json

# Load existing books
with open("books.json", "r", encoding="utf-8") as f:
    books = json.load(f)

# Add new book
new_book = {"id": 3, "title": "Python Basics", "author": "John Doe"}
books.append(new_book)

# Update a book (find by id)
for b in books:
    if b["id"] == 2:
        b["title"] = "Clean Code (Updated)"

# Delete a book (remove by id)
books = [b for b in books if b["id"] != 1]

# Save back to file
with open("books.json", "w", encoding="utf-8") as f:
    json.dump(books, f, indent=2)

print("Books updated successfully!")

This shows how to add, update, and delete items in a JSON file.

Task 4: Movie Recommendation (OMDb API)
import requests
import random

# Replace with your API key from http://www.omdbapi.com/
API_KEY = "YOUR_API_KEY"
GENRE = "Action"

# OMDb doesn’t support direct genre search, so we search common terms
URL = f"http://www.omdbapi.com/?s=man&type=movie&apikey={API_KEY}"
response = requests.get(URL)
data = response.json()

if data["Response"] == "True":
    movies = data["Search"]

    # Pick random movie from search results
    chosen = random.choice(movies)
    imdb_id = chosen["imdbID"]

    # Get full details
    details_url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={API_KEY}"
    details_resp = requests.get(details_url)
    details = details_resp.json()

    if GENRE.lower() in details.get("Genre", "").lower():
        print("Recommended Movie:")
        print("Title:", details["Title"])
        print("Year:", details["Year"])
        print("Genre:", details["Genre"])
        print("Plot:", details["Plot"])
    else:
        print("No movie found in this genre with current search.")
else:
    print("Error fetching movies:", data.get("Error"))


