import pandas as pd
import numpy as np

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
