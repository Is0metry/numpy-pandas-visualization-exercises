from audioop import maxpp
from pydataset import data

import pandas as pd
import numpy as np

#Q1: Copy the code from the lesson to create a dataframe full of student grades.
np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

# Pt. A-Create a column named passing_english that indicates whether each student has a passing grade in english.
print('Part A:')
df['passing_english'] = df.english > 70
print(df)
print()

# Pt. B-Sort the english grades by the passing_english column. How are duplicates handled?
print('Part B')
print(df.sort_values('passing_english'))
print()
# Items are sorted by the designated value first,
# and then by index
# Pt. C-Sort the english grade first by passing_english (failing first) then by name.
print('Part C:')
print(df.sort_values(by=['passing_english','name']))
print()
# Pt. D-Sort the english grades first by passing_english, and then by the actual english grade
print('Part D:')
print(df.sort_values(by=['passing_english','english'],ascending=[True,False]))
print()
# Pt. E-Calculate each students overall grade and add it as a column on the dataframe. 
print('Part E:')
df['overall_grade'] = round((df.math + df.english + df.reading)/3,1)
print(df)
print()

# Q2-Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
mpg = data('mpg')
# Pt. 1-How many rows and columns are there?
print('Part 1:')
print(mpg.shape)
print()

# Pt. 2-What are the data types of each column?
print('Part 2:')
print(mpg.dtypes)
print()

# Pt. 3-Summarize the dataframe with .info and .describe
print('Part 3:')
print(mpg.describe())
print(mpg.info())
print()
# Pt. 4 & 5-rename cty to city and hwy to highway
print('Part 4:')
mpg = mpg.rename(columns={'cty':'city','hwy':'highway'})
print(mpg)
print()
# Pt. 6-Do any cars have better city mileage than highway mileage?
print('Part 6:')
cty_gt_hwy = mpg[mpg.city > mpg.highway]
print(cty_gt_hwy)
#nope (no hybrids I guess?)
print()
# Pt. 7-Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
print('Part 7:')
mpg['mileage_difference'] = mpg.highway - mpg.city
print(mpg[['manufacturer','model','mileage_difference']])
print()
# Pt. 8-Which car (or cars) has the highest mileage difference
print('Part 8:')
print(mpg[['manufacturer','model','mileage_difference']][mpg.mileage_difference == mpg.mileage_difference.max()])
print()
# Pt. 9-Which compact class car has the lowest highway mileage? The best?
print('Part 9:')
compacts = mpg[mpg['class'] == 'compact'] #have to get the column this way otherwise python freaks out on the class keyword
print('Lowest highway MPG:')
print(compacts[['manufacturer','model','highway']][compacts.highway == compacts.highway.min()])
print('Highest highway MPG:')
print(compacts[['manufacturer','model','highway']][compacts.highway == compacts.highway.max()])
print()
# Pt. 10-Create a column named average_mileage that is the mean of the city and highway mileage.
print('Part 10:')
mpg['average_mileage'] = (mpg.city + mpg.highway) / 2
print(mpg[['manufacturer','year','model','average_mileage']])
print()
# Pt. 11- Which dodge car has the best average mileage? The worst?
print('Part 11:')
dodges = mpg[['model','year','average_mileage']][mpg.manufacturer == 'dodge']
print(f'Best mileage:\n {dodges[dodges.average_mileage == dodges.average_mileage.max()]}')
print(f'Worst mileage:\n {dodges[dodges.average_mileage == dodges.average_mileage.min()]}')
print()
print()
#Q3- load the mammals dataset
mammals = data('Mammals')
# Pt. 1-How many rows and columns are there?
print('Part 1:')
print(f'there are {mammals.shape[0]} rows and {mammals.shape[1]} columns.')
print()
# Pt. 2- What are the data types?
print('Part 2:')
print(f'Data Types:\n{mammals.dtypes}')
print()
# Pt. 3-Summarize the dataframe with .info and .describe
print('Part 3:')
print(mammals.info())
print(mammals.describe())
print()
# Pt. 4-What is the the weight of the fastest animal?
print('Part 4:')
print(mammals[['weight','speed']].sort_values(by='speed',ascending=False).head(1))
print()
# Pt. 5-What is the overall percentage of specials?
print('Part 5:')
print(f'Percentage of specials:{round(mammals.specials.sum() / mammals.weight.count() * 100,2)}%')
print()
# Pt. 6-How many animals are hoppers that are above the median speed? What percentage is this?
print('Part 6:')
hoppers_over_median = mammals[(mammals.speed > mammals.speed.median()) & (mammals.hoppers)].hoppers.count()
print(f'hoppers over median speed: {hoppers_over_median}')
print(f'percentage of total: {round(hoppers_over_median / mammals.weight.count() * 100,2)}%')
print()