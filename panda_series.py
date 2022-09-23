import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from helpers import handle_commas,get_letter_grade
fruit_series =  pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
print('Part 1:\n')
#Q1-Determine the number of elements in fruits.
print(f'Q1:\nThere are {fruit_series.size} fruits.\n')
#Q2-Output only the index from fruits.
print('Q2:')
for i in fruit_series.index:
    print(f'index: {i}')
print()
#Q3-Output only the values from fruits.
print('Q3:')
for i in fruit_series.values:
    print(f'value: {i}')
print('\n')
#Q4-Confirm the data type of the values in fruits.
print('Q4:')
try:
    assert(fruit_series.dtype == object)
    print('fruit_series uses dtype object\n')
except AssertionError:
    print(f'Type mismatch! Expected object, received {fruit_series.dtype}\n')
#Q5-Output only the first five values from fruits. Output the last three values. Output two random values from fruits.
print('Q5:')
print(f'first 5 elements of list:\n{fruit_series.head()}')
print(f'Last 3 items:\n{fruit_series.tail(3)}')
print(f'Two random values:\n{fruit_series.sample(2)}')
print()
#Q6-Run the .describe() on fruits to see what information it returns when called on a Series with string values.
print('Q6:')
print(fruit_series.describe())
print()
#Q7-Run the code necessary to produce only the unique string values from fruits.
print('Q7:')
print(f'unique fruits:\n{fruit_series.unique()}')
print()
#Q8-Determine how many times each unique string value occurs in fruits.
print('Q8:')
fruit_value_counts = fruit_series.value_counts()
print(f'item counts:\n{fruit_value_counts}')
print()
#Q9-Determine the string value that occurs most frequently in fruits.
print('Q9:')
print(f'most frequent value: {fruit_value_counts.index[0]}')
#Q10-Determine the string value that occurs least frequently in fruits.
print(f'least frequent value: {fruit_value_counts.index[len(fruit_value_counts)-1]}')
print()
#Part 2
print('Part 2:\n\n')
#Q1-Capitalize all the string values in fruits.
print('Q1:')

print(fruit_series.str.capitalize())
print()
#Q2-Count the letter "a" in all the string values (use string vectorization).
print('Q2:')
print(f'there are {fruit_series.str.count("a").sum()} a\'s in fruit_series.')
print()
#Q3-Output the number of vowels in each and every string value.
print('Q3:')
vowel_count = fruit_series.str.count('[aeiou]+')
vowel_count.index = fruit_series
print(f'Count of vowels:\n{vowel_count}')
print()
#Q4-Write the code to get the longest string value from fruits.
print('Q4:')
string_length = fruit_series.str.len()
string_length.index = fruit_series
longest_string = string_length.idxmax()
longest_len = string_length.max()
print(f'longest string: {longest_string} at {longest_len} chars long.')
print()
# Q5-Write the code to get the string values with 5 or more letters in the name.
print('Q5:')
print(f'values with 5 or more characters:\n{fruit_series[fruit_series.str.len() > 5]}\n')
print()
# Q6 - Find the fruit(s) containing the letter "o" two or more times.
print('Q6:')
print(f'Fruits with two or more o\'s:\n{fruit_series[fruit_series.str.count("o") > 1]}')
print()
# Q7 - Write the code to get only the string values containing the substring "berry".
print('Q7:')
print(f'strings containing "berry":\n{fruit_series[fruit_series.str.contains("berry")]}')
print()
# Q8 - Write the code to get only the string values containing the substring "apple".
print('Q8:')
print(f'strings containing "apple":\n{fruit_series[fruit_series.str.contains("apple")]}')
print()
#Q9 - Which string value contains the most vowels?
print('Q9:')
max_vowel_index = vowel_count.idxmax()
print(f'string with the most vowels is {max_vowel_index} with {vowel_count[max_vowel_index]}')
print()

#Part III
print('Part III\n')
letters = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))
#Q1-Which letter occurs the most frequently in the letters Series?
print('Q1:')
letter_val_counts = letters.value_counts().sort_values(ascending=False)
letter_head = letter_val_counts.head(1)
print(f'Character {letter_head.index.values[0]} occurs the most ({letter_head.values[0]} times).')
print()
#Q2-Which letter occurs the Least frequently?
print('Q2:')
letter_tail = letters.tail(1)
print(f'Character {letter_tail.index.values[0]} occurs the least ({letter_head.values[0]} times).')
print()
#Q3-How many vowels are in the Series?
vowels = list('aeiou')
print(f'there are {letters.isin(vowels).sum()} vowels in the series')
print()
#Q4-How many consonants are in the Series?
print('Q4:')
print(f'There are {(~letters.isin(vowels)).sum()} consonants in the series.')
print()
#Q5-Create a Series that has all of the same letters but uppercased.
upper_letter_series = letters.apply(lambda x: x.upper())
print(f'Q5:\n{upper_letter_series}\n')
#Q6-Create a bar plot of the frequencies of the 6 most commonly occuring letters.
letter_val_counts.head(5).plot.bar(title='Letter Frequencies',rot=0,color='blue',ec='black',width=.9).set(xlabel='Letter',ylabel='Frequency')
plt.show()
print()
#setup for next set of questions
numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])
#Q1-What is the data type of the numbers Series?
print('Q1:')
print(f'Data type of \'numbers\': {numbers.dtype}')
print()
#Q2 - How many elements are in the number Series?
print('Q2:')
print(f'There are {numbers.count()} items in \'numbers\'')
print()
# Q3-Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.
print('Q3:')
numbers = numbers.apply(lambda x: handle_commas(x[1:]) * 100).astype('int')
numbers.apply(lambda x: print(f'${x // 100}.{x%100}'))
print()
# Q4-Run the code to discover the maximum value from the Series.
print('Q4:')
max_numbers = numbers.max()
print(f'Maximum value in numbers is: ${max_numbers //100}.{max_numbers % 100}')
print()
# Q5-Run the code to discover the minimum value from the Series.
print(f'Q5:')
min_numbers = numbers.min()
print(f'Minimum value in numbers is: ${min_numbers //100}.{min_numbers % 100}')
print()
# Q6-What is the range of the values in the Series?
print(f'Q6:')
range_numbers = max_numbers - min_numbers
print(f'Range of values: ${range_numbers // 100}.{range_numbers % 100}')
print()
# Q7-Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
print(f'Q7:')
number_bins = pd.cut(numbers,4).value_counts()
print(f'Binned values of numbers:\n{number_bins}')
print()
# Q8-Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
plt.clf()
number_bins.plot.bar(title='Occurence of values in numbers',rot=0,color='firebrick',ec='black').set(xlabel='value range',ylabel='frequency')
plt.show()

#setup for next section
exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])
# Q1-How many elements are in the exam_scores Series?
print(f'Q1:')
print(f'There are {exam_scores.count()} in exam_scores')
print()
# Q2-Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.
print(f'Q2:')
# Saving this for later
max_score = exam_scores.max()
print(f'Mean of data: {exam_scores.mean()}')
print(f'Median of data: {exam_scores.median()}')
print(f'Minimum of data: {exam_scores.min()}')
print(f'Maximum of data: {exam_scores.max()}')
print()
# Q3-Plot the Series in a meaningful way and make sure your chart has a title and axis labels.
plt.clf()
exam_scores.plot.hist(title='Distribution of Grades',bins=10,rot=0,color='navy',ec='red').set(xlabel='score',ylabel='count')
plt.show()
# Q4-Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. Add the necessary points to the highest grade to make it 100, and add the same number of points to every other score in the Series as well.
curved_grades = exam_scores.apply(lambda x:x + (100 - max_score))

# Q5-Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.
letter_grades = curved_grades.apply(get_letter_grade)
# Q6-Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.
plt.clf()
letter_grades.value_counts().plot.pie(title="Letter Grade Percentages",rot=0).set(ylabel='')
plt.show()