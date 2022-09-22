import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

print(f'There are {(a < 0).sum()} negative values')
print(f'There are {(a > 0).sum()} positive values')
even_positive = np.bitwise_and(a > 0, a % 2 == 0).sum()
print(f'There are {even_positive} even positive values.')
b = a+3
even_positive = np.bitwise_and(b > 0, b % 2 == 0).sum()
print(f'There are {even_positive} even positive values if you add 3.')
b = a ** 2
print(f'the mean after squaring is {b.mean()} and the standard deviation is {b.std()}')

a_mean = a.mean()
b = a - a_mean
print(f'centered falues are:\n {b}.')
z = b / a.std()
print(f'z-scores for the data points: \n {z}')

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum(a) / len(a)
# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = a[0]
for i in a[1:]:
    product_of_a *= i
# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = []
for i in a:
    squares_of_a.append(i * i)
# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = []
for i in a:
    if i % 2 !=0:
        odds_in_a.append(i)
# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
for i in a:
    if i % 2 ==0:
        odds_in_a.append(i)
## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = np.array([
    [3, 4, 5],
    [6, 7, 8]
])

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = b.sum()

# Exercise 2 - refactor the following to use numpy. 
min_of_b = b.min()
# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = b.max()


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = b.mean()

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = b.prod()

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = np.reshape(b ** 2, 6)
# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = b[b % 2 !=0]

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = b[b % 2 == 0]

# Exercise 9 - print out the shape of the array b.
print(f'Shape of b: {b.shape}')
# Exercise 10 - transpose the array b
b = np.transpose(b)
# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b = np.reshape(b,6)
# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b = np.reshape(b,(6,1))
print(b)

## Setup 3
c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
min_of_c = c.min()
max_of_c = c.max()
sum_of_c = c.sum()
product_of_c = c.prod()
# Exercise 2 - Determine the standard deviation of c.
std_of_c = c.std()
# Exercise 3 - Determine the variance of c.
variance_of_c = c.var()
# Exercise 4 - Print out the shape of the array c
print(f'shape of C: {c.shape}.')
# Exercise 5 - Transpose c and print out transposed result.
print(np.transpose(c))
# Exercise 6 - Get the dot product of the array c with c. 
dot_prod_of_c = c.dot(c)
# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
c_trans_c_sum = (c * np.transpose(c)).sum()
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
c_trans_c_prod = (c * np.transpose(c)).prod()


## Setup 4
d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
])

# Exercise 1 - Find the sine of all the numbers in d
sine = np.sin(d)
# Exercise 2 - Find the cosine of all the numbers in d
cosine = np.cos(d)
# Exercise 3 - Find the tangent of all the numbers in d
tangent = np.tan(d)
# Exercise 4 - Find all the negative numbers in d
neg_in_d = d[d < 0]
# Exercise 5 - Find all the positive numbers in d
pos_in_d = d[d > 0]
# Exercise 6 - Return an array of only the unique numbers in d.
unique_in_d = np.unique(d)
# Exercise 7 - Determine how many unique numbers there are in d.
unique_in_d_count = len(unique_in_d)
# Exercise 8 - Print out the shape of d.
print(f'shape of d: {d.shape}')
# Exercise 9 - Transpose and then print out the shape of d.
print(f'shape of d: {d.transpose().shape}')
# Exercise 10 - Reshape d into an array of 9 x 2
reshaped_d = d.reshape((9,2))