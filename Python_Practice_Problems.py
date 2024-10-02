# Simple arithmetic modulo
print(8 % 3)

# Length of a concatenated string
print(len("Hi" + "5"))

# Accessing a sorted list
numbers = [3, 1, 4, 1]
numbers.sort()
print(numbers[1])

# Type checking, simplified
x = 15
print(x > 10)

# Function return modified
def func(x):
  return x % 4
print(func(9))

# Converting and adding
x = "9"
y = 1
print(int(x) % y)

# Repetition and slicing
x = "fun"
print((x * 2)[2])

# Boolean logic simplified
x = False
y = True
print(x or y)

# Slicing a list
list = [1, 2, 3, 4]
print(list[3] - 3)

# Equality test
x = 5
y = x == 5
print(int(y))

# Simple division
print(10 // 4)

# Count characters in a string
print(len("PythonRocks!"))

# Find the minimum in a list
numbers = [5, 9, 3, 6]
print(min(numbers))

# Boolean comparison
x = 20
print(x < 25)

# Calculate remainder using a function
def get_remainder(x, y):
    return x % y
print(get_remainder(18, 4))

# Combine integers into a string
x = 4
y = 5
print(str(x) + str(y))

# Indexing and slicing
word = "programming"
print(word[-3])

# Logical NOT
x = True
print(not x)

# Use slicing to reverse a string
text = "hello"
print(text[::-1])

# Checking if two conditions are true
x = 7
y = 10
print(x > 5 and y < 15)

# Invert a dictionary (swap keys and values)
original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = {value: key for key, value in original_dict.items()}
print(inverted_dict)

# Create a complex number and print its real and imaginary parts
complex_number = 3 + 4j
print(complex_number.real, complex_number.imag)

# Check if a list is empty
empty_list = []
print(not empty_list)

# Check if a list is empty
empty_list = [1, 2, 3]
print(not empty_list)

# Format strings using f-string
name = "John"
age = 30
print(f"{name} is {age} years old.")

# Calculate the length of a tuple
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))

# Find the intersection of two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 & set2)

# Convert a list of integers to a comma-separated string
numbers = [1, 2, 3, 4, 5]
print(','.join(map(str, numbers)))

# Check if a string is a palindrome
word = "radar"
print(word == word[::-1])

# Remove all occurrences of an element from a list
items = [1, 2, 3, 2, 4, 2, 5]
filtered_items = [item for item in items if item != 2]
print(filtered_items)


# Find the maximum value in a dictionary
score_dict = {'Alice': 88, 'Bob': 95, 'Carol': 84}
max_score = max(score_dict.values())
print(max_score)

# Unpack elements from a list into variables
elements = [1, 2, 3]
a, b, c = elements
print(a, b, c)

# Use a slice to clear all elements from a list
data = [1, 2, 3, 4, 5]
data[:] = []
print(data)

# Find the most frequent element in a list
from collections import Counter
freq_list = [1, 2, 3, 2, 4, 2, 5, 3, 3]
most_common = Counter(freq_list).most_common(1)
print(most_common[0][0])

# Check for the presence of a key in a dictionary
key_check_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_check = 'b'
print(key_to_check in key_check_dict)

# Calculate the Euclidean distance between two points in 2D
from math import sqrt
point1 = (1, 2)
point2 = (4, 6)
distance = sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
print(distance)

# Create a set from a string, showing unique characters
unique_chars = set('hello world')
print(unique_chars)

# Convert a string to lowercase
upper_str = "THIS IS AN UPPERCASE STRING"
print(upper_str.lower())

# Calculate the sum of squares of a range of numbers
sum_of_squares = sum(x**2 for x in range(10))
print(sum_of_squares)

# Use a dictionary comprehension to create a dictionary of squares
squares_dict = {x: x**2 for x in range(6)}
print(squares_dict)

# Output a list of even numbers from a given list
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = [num for num in numbers_list if num % 2 == 0]
print(evens)

# Find the minimum in a list
numbers = [5, 9, 3, 6]
print(min(numbers))

# Boolean comparison
x = 20
print(x < 25)

# Calculate remainder using a function
def get_remainder(x, y):
    return x % y
print(get_remainder(18, 4))

# Combine integers into a string
x = 4
y = 5
print(str(x) + str(y))

# Indexing and slicing
word = "programming"
print(word[-3])

# Logical NOT
x = True
print(not x)

# Use slicing to reverse a string
text = "hello"
print(text[::-1])

# Checking if two conditions are true
x = 7
y = 10
print(x > 5 and y < 15)

# Checking if two conditions are true
x = 7
y = 10
print(x > 5 or y < 15)

# Create a list and append an item
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

# Multiply elements in a list
nums = [2, 4, 6]
result = [x * 2 for x in nums]
print(result)

# Generating a dictionary from two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print(my_dict)

# Convert integer to binary
number = 10
print(bin(number)[2:])

# Generate a list of squares using list comprehension
squares = [x**2 for x in range(10)]
print(squares)

# Calculate the sum of all numbers in a list
squares = [x**2 for x in range(10)]
print(sum(squares))

# Using map to convert strings to upper case
names = ["alice", "bob", "carol"]
print(map(str.upper, names))

# Using filter to find even numbers
evens = (filter(lambda x: x % 2 == 0, range(10)))
print(evens)

# Using a set to remove duplicates from a list
duplicates = [1, 2, 2, 3, 3, 3, 4]
unique_items = set(duplicates)
print(unique_items)

# Check if a substring is in a string
phrase = "Hello world"
print("world" in phrase)

# Using enumerate to get index and value from a list
for index, value in enumerate(['a', 'b', 'c']):
    print(f"Index {index}: {value}")

# Calculate factorial using a recursive function
n=5
while n > 1:
 count = n * n-1
 n  = n-1
print(count)

# Using a try-except block to handle division by zero
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# Using a lambda function to sort a list of tuples by second item
items = [(1, 2), (3, 1), (5, 0)]
items.sort(key=lambda x: x[1])
print(items)

# Concatenating multiple lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
combined_list = list1 + list2 + list3
print(combined_list)

# Check if all elements in a list are True
bools = [True, True, False]
print(all(bools))

# Using zip to combine two lists into a list of tuples
names = ['Alice', 'Bob', 'Cindy']
ages = [25, 30, 35]
people = (zip(names, ages))
print(people)

# Simple arithmetic modulo
print(8 % 3)

# Length of a concatenated string
print(len("Hi" + "5"))

# Accessing a sorted list
numbers = [3, 1, 4, 1]
numbers.sort()
print(numbers[1])

# Type checking, simplified
x = 15
print(x > 10)

# Function return modified
def func(x):
  return x % 4
print(func(9))

# Converting and adding
x = "9"
y = 1
print(int(x) % y)

# Repetition and slicing
x = "fun"
print((x * 2)[2])

# Boolean logic simplified
x = False
y = True
print(x or y)

# Slicing a list
list = [1, 2, 3, 4]
print(list[3] - 3)

# Equality test
x = 5
y = x == 5
print(int(y))

# Simple division
print(10 // 4)

# Count characters in a string
print(len("PythonRocks!"))

# Calculate the cube of a number
num = 3
print(num ** 3)

# Find the index of an element in a list
fruits = ['apple', 'banana', 'cherry']
print(fruits.index('banana'))

# Check if a string is uppercase
word = "HELLO"
print(word.isupper())

# Create a dictionary with default values using fromkeys
keys = ['name', 'age', 'gender']
defaults = 'unknown'
person = dict.fromkeys(keys, defaults)
print(person)

# Get the absolute value of a number
number = -7
print(abs(number))

# Find the maximum of three numbers
a, b, c = 5, 10, 3
print(max(a, b, c))

# Convert a string to title case
sentence = "python is fun"
print(sentence.title())

# Sort a list of tuples by the second element
students = [('John', 85), ('Jane', 90), ('Dave', 80)]
students.sort(key=lambda student: student[1])
print(students)

# Create a list of characters from a string
string = "hello"
char_list = list(string)
print(char_list)

# Check if all characters in a string are alphanumeric
alpha_num = "Python123"
print(alpha_num.isalnum())

# Replace a substring in a string
text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text)

# Calculate the area of a circle
import math
radius = 5
area = math.pi * (radius ** 2)
print(area)

# Flatten a nested list
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)

# Check if a list contains a specific element
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)

# Create a list of even numbers using range
evens = list(range(0, 21, 2))
print(evens)

# Calculate the length of a set
unique_numbers = {1, 2, 3, 4, 5}
print(len(unique_numbers))

# Create a list of squares using map
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

# Print the keys of a dictionary
person = {'name': 'Alice', 'age': 25, 'gender': 'Female'}
print(person.keys())

# Create a set from a list
items = [1, 2, 3, 1, 2, 3]
unique_items = set(items)
print(unique_items)

# Remove an element from a list by index
colors = ['red', 'green', 'blue']
del colors[1]
print(colors)

# Check if a string ends with a specific suffix
filename = "report.pdf"
print(filename.endswith(".pdf"))

# Use a generator expression to create an iterable of squares
squares_gen = (x ** 2 for x in range(10))
print(list(squares_gen))