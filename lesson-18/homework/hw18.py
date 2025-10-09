Here are my answers: 

Homework question 2 – stackoverflow_qa.csv
import pandas as pd

# Load the data
df = pd.read_csv('task\\stackoverflow_qa.csv')

# Display first few rows
print(df.head())

1 Find all questions that were created before 2014
df['creationdate'] = pd.to_datetime(df['creationdate'])
before_2014 = df[df['creationdate'] < '2014-01-01']
print(before_2014)

2 Find all questions with a score more than 50
high_score = df[df['score'] > 50]
print(high_score)

3 Find all questions with a score between 50 and 100
score_range = df[(df['score'] >= 50) & (df['score'] <= 100)]
print(score_range)

4 Find all questions answered by Scott Boston
scott_boston = df[df['ans_name'] == 'Scott Boston']
print(scott_boston)

5 Find all questions answered by the following 5 users
users = ['Scott Boston', 'Unutbu', 'Mike Pennington', 'Demitri', 'doug']
answered_by_5 = df[df['ans_name'].isin(users)]
print(answered_by_5)

6 Find all questions created between March 2014 and October 2014 that were answered by Unutbu and have a score less than 5
mask = (
    (df['creationdate'] >= '2014-03-01') &
    (df['creationdate'] <= '2014-10-31') &
    (df['ans_name'] == 'Unutbu') &
    (df['score'] < 5)
)
unutbu_period = df[mask]
print(unutbu_period)

7 Find all questions that have a score between 5 and 10 or have a view count greater than 10,000
filtered = df[(df['score'].between(5, 10)) | (df['viewcount'] > 10000)]
print(filtered)

8 Find all questions that are not answered by Scott Boston
not_scott = df[df['ans_name'] != 'Scott Boston']
print(not_scott)

Homework question 3 – titanic.csv
import pandas as pd

titanic_df = pd.read_csv("task\\titanic.csv")
print(titanic_df.head())

1 Female Passengers in Class 1 (Age 20–30)
female_class1 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'].between(20, 30))
]
print(female_class1)

2 Passengers Who Paid More than $100
fare_over_100 = titanic_df[titanic_df['Fare'] > 100]
print(fare_over_100)

3 Passengers Who Survived and Were Traveling Alone
alone_survivors = titanic_df[
    (titanic_df['Survived'] == 1) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]
print(alone_survivors)

4 Passengers Embarked from 'C' and Paid More Than $50
embarked_c = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]
print(embarked_c)

5 Passengers with Both Siblings/Spouses and Parents/Children
both_relatives = titanic_df[
    (titanic_df['SibSp'] > 0) &
    (titanic_df['Parch'] > 0)
]
print(both_relatives)

6 Passengers Aged 15 or Younger Who Did Not Survive
young_not_survived = titanic_df[
    (titanic_df['Age'] <= 15) &
    (titanic_df['Survived'] == 0)
]
print(young_not_survived)

7 Passengers with Known Cabins and Fare > $200
high_fare_cabin = titanic_df[
    (titanic_df['Cabin'].notnull()) &
    (titanic_df['Fare'] > 200)
]
print(high_fare_cabin)

8 Passengers with Odd-Numbered Passenger IDs
odd_id = titanic_df[titanic_df['PassengerId'] % 2 != 0]
print(odd_id)

9 Passengers with Unique Ticket Numbers
unique_tickets = titanic_df[
    ~titanic_df.duplicated(subset='Ticket', keep=False)
]
print(unique_tickets)

10 Female Passengers with “Miss” in Name and in Class 1
miss_class1 = titanic_df[
    (titanic_df['Name'].str.contains('Miss')) &
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1)
]
print(miss_class1)

