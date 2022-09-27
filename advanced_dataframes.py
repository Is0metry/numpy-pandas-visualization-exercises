from datetime import date
from env import host,user,password
import sqlalchemy
import pandas as pd
import numpy as np

mysql_limit = 10000
# enforce_limit is a helper function which returns a LIMIT clause if limit_on is >0. This is to 
# help with performance while debugging
def enforce_limit(limit):
    return f'LIMIT {limit};' if limit > 0 else ';'

#Q3-Create a function named get_db_url. It should accept a username, hostname, password, 
# and database name and return a url connection string formatted like in the example at the start of this lesson.
def get_db_url(host,uname,passwrd):
    return f'mysql+pymysql://{uname}:{passwrd}@{host}/employees'
# Q4-Use your function to obtain a connection to the employees database.
print(f'Q4:')

url = get_db_url(host,user,password)

employees_df = pd.read_sql('SELECT * FROM employees LIMIT 50;',url)
print(employees_df.head(5))
print()
# Q5-Use your function to obtain a connection to the employees database.
print(f'Q5:')
# Pt. A-Intentionally make a typo in the database url. What kind of error message do you see?
print('Part A:')
bad_url = get_db_url('blah','blah','blah')
try:
    error_df = pd.read_sql('SELECT * FROM employees LIMIT 50;',bad_url)
except Exception as e:
    print(f'On bad URL, received error: {e.args}')
# Pt. B-Intentionally make an error in your SQL query. What does the error message look like?
print('Part B:')
try:
    error_df = pd.read_sql('SELECT blah FROM employees LIMIT 5;',url)
except Exception as e:
    print(f'On bad SQL, received error: {e.args}')
print()
print()
# Q6-Read the employees and titles tables into two separate DataFrames.
print(f'Q6:')
employees_df = pd.read_sql(f'SELECT * FROM employees {enforce_limit(mysql_limit)}',url)
print('employees loaded into employees_df')
titles_df = pd.read_sql(f'SELECT * FROM titles {enforce_limit(mysql_limit)}',url)
print('titles loaded into titles_df')
print()
# Q7-How many rows and columns do you have in each DataFrame? Is that what you expected?
print(f'Q7:')
print(f'employees_df has {employees_df.shape[0]} rows and {employees_df.shape[1]} columns, which is expected.')
print(f'title_df has {titles_df.shape[0]} rows and {titles_df.shape[1]} columns, which is expected')
print()

# Q8-Display the summary statistics for each DataFrame
print(f'Q8:')
print(f'Summary statistics for employees_df:\n{employees_df.describe()}\n')
print(f'Summary statistics for titles_df:\n{titles_df.describe()}\n')
print()

# Q9-How many unique titles are in the titles DataFrame?
print(f'Q9:')
unique_titles = len(titles_df.title.unique())
print(f'there are {unique_titles} unique titles in titles_df.')
print()

# Q10-What is the oldest date in the to_date column?
print(f'Q10:')
query = '''SELECT * FROM titles ORDER BY to_date ASC LIMIT 1;'''
oldest_date = pd.read_sql(query,url)
print(f'Oldest date is:\n{oldest_date}')
print()

# Q11-What is the most recent date in the to_date column?
print(f'Q11:')
print(titles_df.dtypes)
newest_date = titles_df[titles_df.to_date < date.today()].sort_values(by='to_date',ascending=False).head(1)
print(f'Most recent date is:\n{newest_date}')
print('\n\n\n')



#Exercises II
