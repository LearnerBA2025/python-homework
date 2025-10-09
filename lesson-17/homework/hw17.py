Here are my answers: 
Question 1:
import pandas as pd
import numpy as np  # for random salary values

# Original data
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

# Create DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# 1️⃣ Rename columns
df.rename(columns={'First Name': 'first_name', 'Age': 'age'}, inplace=True)
print("\nRenamed Columns:\n", df)

# 2️⃣ Print first 3 rows
print("\nFirst 3 rows:\n", df.head(3))

# 3️⃣ Find mean age
mean_age = df['age'].mean()
print("\nMean Age:", mean_age)

# 4️⃣ Select and print only 'first_name' and 'City'
print("\nSelected Columns ('first_name' and 'City'):\n", df[['first_name', 'City']])

# 5️⃣ Add new column 'Salary' with random values
df['Salary'] = np.random.randint(4000, 9000, size=len(df))
print("\nAfter Adding Salary Column:\n", df)

# 6️⃣ Display summary statistics
print("\nSummary Statistics:\n", df.describe())

Original DataFrame:
  First Name  Age           City
0      Alice   25       New York
1        Bob   30  San Francisco
2    Charlie   35    Los Angeles
3      David   40        Chicago

Renamed Columns:
  first_name  age           City
0      Alice   25       New York
1        Bob   30  San Francisco
2    Charlie   35    Los Angeles
3      David   40        Chicago

First 3 rows:
  first_name  age           City
0      Alice   25       New York
1        Bob   30  San Francisco
2    Charlie   35    Los Angeles

Mean Age: 32.5

Selected Columns ('first_name' and 'City'):
  first_name           City
0      Alice       New York
1        Bob  San Francisco
2    Charlie    Los Angeles
3      David        Chicago

After Adding Salary Column:
  first_name  age           City  Salary
0      Alice   25       New York   7085
1        Bob   30  San Francisco   5201
2    Charlie   35    Los Angeles   8900
3      David   40        Chicago   4567

Summary Statistics:
              age       Salary
count   4.000000     4.000000
mean   32.500000  6438.250000
std     6.454972  2022.346537
min    25.000000  4567.000000
max    40.000000  8900.000000


Question 2: Sales and Expenses
import pandas as pd

# Create DataFrame
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}
sales_and_expenses = pd.DataFrame(data)

print("Sales and Expenses DataFrame:\n", sales_and_expenses)

# 1️⃣ Maximum values
print("\nMaximum Sales:", sales_and_expenses['Sales'].max())
print("Maximum Expenses:", sales_and_expenses['Expenses'].max())

# 2️⃣ Minimum values
print("\nMinimum Sales:", sales_and_expenses['Sales'].min())
print("Minimum Expenses:", sales_and_expenses['Expenses'].min())

# 3️⃣ Average values
print("\nAverage Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())

Maximum Sales: 8000
Maximum Expenses: 4500
Minimum Sales: 5000
Minimum Expenses: 3000
Average Sales: 6625.0
Average Expenses: 3750.0

Question 3: Monthly Expenses by Category
import pandas as pd

# Create DataFrame
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

expenses = pd.DataFrame(data)
print("Original Expenses DataFrame:\n", expenses)

# Set Category as index
expenses = expenses.set_index('Category')
print("\nDataFrame with Category as Index:\n", expenses)

# 1️⃣ Maximum expense per category
max_expense = expenses.max(axis=1)
print("\nMaximum expense per category:\n", max_expense)

# 2️⃣ Minimum expense per category
min_expense = expenses.min(axis=1)
print("\nMinimum expense per category:\n", min_expense)

# 3️⃣ Average expense per category
avg_expense = expenses.mean(axis=1)
print("\nAverage expense per category:\n", avg_expense)

Maximum expense per category:
Category
Rent             1500
Utilities         250
Groceries         350
Entertainment     180
dtype: int64

Minimum expense per category:
Category
Rent             1200
Utilities         200
Groceries         300
Entertainment     150
dtype: int64

Average expense per category:
Category
Rent             1350.0
Utilities         227.5
Groceries         325.0
Entertainment     165.0
dtype: float64
