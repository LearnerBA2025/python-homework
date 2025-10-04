Here are my answers: 
import sqlite3

# 1 Create (or connect to) a database file
connection = sqlite3.connect("roster.db")  # creates file if it doesn't exist
cursor = connection.cursor()

# 2️ Create a new table named Roster
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# 3️ Insert the provided records
roster_data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.executemany("INSERT INTO Roster VALUES (?, ?, ?)", roster_data)

# 4️ Update the Name of 'Jadzia Dax' → 'Ezri Dax'
cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")

# 5️ Display Name and Age of everyone classified as 'Bajoran'
cursor.execute("""
SELECT Name, Age FROM Roster
WHERE Species = 'Bajoran'
""")

# Fetch and print results
results = cursor.fetchall()
print("Bajoran members:")
for row in results:
    print(f"Name: {row[0]}, Age: {row[1]}")

# 6️ Save changes and close the connection
connection.commit()
connection.close()
