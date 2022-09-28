from datetime import date
from turtle import title
from env import host,user,password,get_db_url
from pydataset import data
import sqlalchemy
import pandas as pd
import numpy as np

mysql_limit = 10
run_tuple = (False,False,True)
# enforce_limit is a helper function which returns a LIMIT clause if limit_on is >0. This is to 
# help with performance while debugging
def enforce_limit(limit):
    return f' LIMIT {limit};' if limit > 0 else ';'

#Q3-Create a function named get_db_url. It should accept a username, hostname, password, 
# and database name and return a url connection string formatted like in the example at the start of this lesson.
'''see helpers.py for get_db_url function'''
url = get_db_url(host,user,password,'employees')
# Q4-Use your function to obtain a connection to the employees database.
if run_tuple[0]:
    print(f'Q4:')


    employees_df = pd.read_sql('SELECT * FROM employees LIMIT 50;',url)
    print(employees_df.head(5))
    print()
    # Q5-Use your function to obtain a connection to the employees database.
    print(f'Q5:')
    # Pt. A-Intentionally make a typo in the database url. What kind of error message do you see?
    print('Part A:')
    bad_url = get_db_url('blah','blah','blah','blah')
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
if run_tuple[1]:
    print('Exercise II')
    # Q1-Copy the users and roles from the example

    # Create the users DataFrame.
    users = pd.DataFrame({
        'id': [1, 2, 3, 4, 5, 6],
        'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
        'role_id': [1, 2, 3, 3, np.nan, np.nan]
    })
    # Create the roles DataFrame

    roles = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'name': ['admin', 'author', 'reviewer', 'commenter']
    })

    # Q2-What is the result of using a right join on the DataFrames?
    print(f'Q2:')
    right_join = users.merge(roles,how='right',left_on='role_id',right_on='id')
    print(f'table after right join:\n{right_join}')
    print()

    # Q3-What is the result of using an outer join on the DataFrames?
    print(f'Q3:')
    outer_join = users.merge(roles,how='outer',left_on='role_id', right_on='id')
    print(f'table after outer join:\n{outer_join}')
    print()
    # Q4- What happens if you drop the foreign keys and then try to merge?
    print(f'Q4:')
    drop_fk_user = users.drop(columns='role_id')
    try:
        drop_fk_user.merge(roles,right_on='id')
    except Exception as e:
        print(f'error when merging: {str(e)}')
    
    # Q5-Load the mpg dataset from PyDataset.
    print(f'Q5:')
    mpg = data('mpg')
    print('mpg dataset loaded as mpg_df')
    print(mpg.head(10))
    print()

    # Q6-Output and read the documentation for the mpg dataset
    print(f'Q6:')
    data('mpg',show_doc=True)
    print()

    # Q7-How many rows and columns are in the dataset?\
    print(f'Q7:')
    print(f'mpg has {mpg.shape[0]} rows and {mpg.shape[1]} columns.')
    print()

    # Q8-Check out your column names and perform any cleanup you may want on them.
    print(f'Q8:')
    print(f'before cleanup:\n{mpg.columns}')
    mpg.rename(columns={'trans':'transmission','drv':'drivetrain',\
        'cyl':'cylinder_count','cty':'city','hwy':'highway','displ':'displacement','fl':'fuel_type'},inplace=True)
    print(f'after cleanup:\n{mpg.columns}')
    print()
    
    # Q9-Display the summary statistics for the dataset.
    print(f'Q9:')
    print(mpg[['city','highway','cylinder_count']].agg(['mean','median','min','max']))
    print()

    # Q10-How many different manufacturers are there?
    print(f'Q10:')
    manufacturers = mpg.groupby('manufacturer')
    print(f'There are {len(manufacturers)} manufacturers.')
    print()

    # Q11-How many different models are there?
    print(f'Q11:')
    models = mpg.groupby('model')
    print(f'There are {len(models)} models.')
    print()
    # Q12-Create a column named mileage_difference like you did in the DataFrames exercises; this column should contain the difference between highway and city mileage for each car.
    mpg['mileage_difference'] = mpg.highway - mpg.city

    #Q13-Create a column named average_mileage like you did in the DataFrames exercises; this is the mean of the city and highway mileage.
    mpg['average_mileage'] = round(2 / ((1/mpg.highway) + (1/mpg.city)), 2)
    # Q14-Create a new column on the mpg dataset named is_automatic that holds boolean values denoting whether the car has an automatic transmission.
    print(f'Q14:')
    mpg['is_automatic'] = np.where(mpg.transmission.str.startswith('a'),True,False)
    print(mpg)
    print()

    # Q15-Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?
    print(f'Q15:')
    mfct_mpg = mpg.groupby('manufacturer').average_mileage.agg('mean').sort_values(ascending=False)
    print(f'The manufacturer with the best average_mileage is {mfct_mpg.head(1).index[0]} with {mfct_mpg.head(1)[0]}.')
    print()

    # Q16-Do automatic or manual cars have better miles per gallon?
    print(f'Q16:')
    automatics = mpg[mpg.is_automatic].average_mileage.mean()
    manuals = mpg[~mpg.is_automatic].average_mileage.mean()
    print(f'{"automatic" if automatics > manuals else "manual"} transmissions have beter mileage than {"manual" if automatics > manuals else "automatic"} ones.')
    print('\n\n\n')
#Exercises III
if run_tuple[2]:
    print('EXERCISES III\n')
    # Q1-Use your get_db_url function to help you explore the data from the chipotle database.
    print(f'Q1:')
    chipotle_url = get_db_url(host,user,password,'chipotle')
    # chipotle only has 1 tabl
    orders_df = pd.read_sql('SELECT * FROM orders;',chipotle_url)
    print(orders_df.dtypes)
    #converting price into numeric values
    orders_df.item_price = orders_df.item_price.apply(lambda p: pd.to_numeric(p[1:]))
    print(orders_df[['id','order_id','quantity','item_name','item_price']])
    print()
    # Q2-What is the total price for each order?
    print(f'Q2:')
    order_sums = orders_df.groupby('order_id').agg('sum').drop(columns=['id']).rename({'item_price':'order_total'})
    print(order_sums)
    print()

    # Q3-What are the 3 most popular items?
    print(f'Q3:')
    items_ordered = orders_df.groupby('item_name').quantity.sum().sort_values(ascending=False).head(3)
    print(f'Three most popular items:\n{items_ordered}')
    print()
    
    # Q4-Which item has produced the most revenue?
    print(f'Q4:')
    item_revenue = orders_df.groupby('item_name').item_price.sum().sort_values(ascending=False).head(1)
    print(f'{item_revenue.index[0]} has produced the most revenue at ${round(item_revenue[0],2)}')
    print()

    # Q5-Join the employees and titles DataFrames together.
    print(f'Q5:')
    #if the database hasn't been loaded in by running Exercises I, load it in
    try:
        len(employees_df)
    except NameError:
        employees_df = pd.read_sql(f'SELECT * FROM employees{enforce_limit(mysql_limit)}',url)
        titles_df = pd.read_sql(f'SELECT * FROM titles{enforce_limit(mysql_limit)}',url)
    employee_title_df = employees_df.merge(titles_df, left_on='emp_no',right_on='emp_no',how='inner')
    print(employee_title_df.head())
    print()
    # Q6-For each title, find the hire date of the employee that was hired most recently with that title.
    print(f'Q6:')
    employee_title_df['hire_date'] = pd.to_datetime(employee_title_df['hire_date'])
    most_recent_hire = employee_title_df.groupby('title').hire_date.idxmax()
    print(employee_title_df[['title','emp_no','first_name','last_name','hire_date']].iloc[most_recent_hire])
    print()

    # Q7-Write the code necessary to create a cross tabulation of the number of titles by department.
    print(f'Q7:')
    q7_query = '''SELECT t.emp_no, t.title, t.to_date, d.dept_name
	FROM departments as d
	JOIN dept_emp AS e USING(dept_no)
	JOIN titles AS t USING(emp_no);'''
    dept_titles_df = pd.read_sql(q7_query,url)
    titles_crosstab = pd.crosstab(dept_titles_df.dept_name, dept_titles_df.title)
    print(titles_crosstab)