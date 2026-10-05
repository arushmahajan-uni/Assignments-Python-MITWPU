# Practice Assignment for Python - Arush Mahajan (Div:13)

#BASICS
#1
print("Student Name:")
print("Address:")
print("Contact No:")
print("Mother Tongue:")
print("School Name:")
print("Year:")
print("Panel:")
print("Roll No:")


#2
print("Student Name:")
"""
print("Address:")
print("Contact No:")
print("Mother Tongue:")
"""
print("School Name:")
print("Year:")
print("Panel:")
print("Roll No:")


#3
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

total = sub1 + sub2 + sub3
percentage = (total / 300) * 100

print("\n Student Details")
print("Name:", name)
print("Roll No:", roll_no)
print("Percentage:", percentage, "%")

if sub1 >= sub2 and sub1 >= sub3:
    print("Highest Marks: Subject 1 (", sub1, ")")
elif sub2 >= sub1 and sub2 >= sub3:
    print("Highest Marks: Subject 2 (", sub2, ")")
else:
    print("Highest Marks: Subject 3 (", sub3, ")")

if sub1 <= sub2 and sub1 <= sub3:
    print("Lowest Marks: Subject 1 (", sub1, ")")
elif sub2 <= sub1 and sub2 <= sub3:
    print("Lowest Marks: Subject 2 (", sub2, ")")
else:
    print("Lowest Marks: Subject 3 (", sub3, ")")


#4
num = float(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")


#5
num = int(input("Enter an integer: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")


#6
num1 = int(input("Enter first non-negative number: "))
num2 = int(input("Enter second non-negative number: "))

last_digit1 = num1 % 10
last_digit2 = num2 % 10

if last_digit1 == last_digit2:
    print(True)
else:
    print(False)


#7
for i in range(1, 11):
    print(i, end="\t")
print()


#8
for num in range(23, 58):
    if num % 2 == 0:
        print(num)


#9
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("It is a prime number")
    else:
        print("Not a prime number")


#10
print("Prime numbers between 10 and 99:")

for num in range(10, 100):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()


#12
num = int(input("Enter a number: "))
temp = abs(num)
reversed_num = 0

while temp > 0:
    digit = temp % 10
    reversed_num = (reversed_num * 10) + digit
    temp = temp // 10

if num < 0:
    reversed_num = -reversed_num

print("Reversed Number:", reversed_num)


#13
num = int(input("Enter a number: "))
original_num = num
reversed_num = 0

temp = abs(num)
while temp > 0:
    digit = temp % 10
    reversed_num = (reversed_num * 10) + digit
    temp = temp // 10

if original_num == reversed_num:
    print("The number is a Palindrome")
else:
    print("The number is not a Palindrome")


#14
for i in range(1, 6):
    n = int(input("Enter number: "))
    cube = n ** 3
    print("Cube of", n, "is:", cube)

#15
num = int(input("Enter a positive number: "))
print("Prime factors:")

factor = 2
while num > 1:
    if num % factor == 0:
        print(factor, end=" ")
        num = num // factor
    else:
        factor += 1
print()


#16
rows = [1, 2,3, 4]
for count in rows:
    print("*" * count)


#Mini Project
#1
distance = float(input("How far do you want to travel (in miles)? "))

if distance < 3:
    print("Ride a bicycle")
elif distance < 300:
    print("Ride a motorcycle")
else:
    print("Drive a supercar")


#2
cost_per_hour = 0.51

cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30 

budget = 918
days_affordable = budget / cost_per_day

print("Cost to operate per day: ", round(cost_per_day, 2))
print("Cost to operate per week: ", round(cost_per_week, 2))
print("Cost to operate per month: ", round(cost_per_month, 2))
print("Days you can operate with 918:", round(days_affordable, 2), "days")


#Data Structures
#1
numbers = [10, 20, 30, 40, 50]

print("Entire list:", numbers)
print("Element at index 0:", numbers[0])
print("Element at index 1:", numbers[1])
print("Element at index 2:", numbers[2])
print("Element at index 3:", numbers[3])
print("Element at index 4:", numbers[4])

#2
my_list = [1, 2, 3, 4]
print("Original list:", my_list)

item = int(input("Enter item to append: "))
my_list.append(item)

print("Updated list:", my_list)

#3
my_list = [10, 20, 30, 40, 50]
print("Original list:", my_list)

my_list.reverse()
print("Reversed list:", my_list)

#4
my_list = [10, 20, 30, 20, 40, 20, 50]
print("List:", my_list)

target = int(input("Enter element to count: "))
count = my_list.count(target)

print("Number of occurrences of", target, ":", count)

#5
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Adding list1 in front of list2
result = list1 + list2
print("Result after appending in front:", result)

#6
my_list = [10, 20, 30, 40]
print("Original list:", my_list)

item = int(input("Enter item to insert: "))
my_list.insert(1, item)

print("Updated list:", my_list)

#7
my_list = [10, 20, 30, 40, 50]
print("Original list:", my_list)

idx = int(input("Enter index to remove item from (0-4): "))
removed_item = my_list.pop(idx)

print("Removed item:", removed_item)
print("Updated list:", my_list)

#8
my_list = [10, 20, 30, 20, 40]
print("Original list:", my_list)

val = int(input("Enter value to remove: "))
if val in my_list:
    my_list.remove(val)
    print("Updated list:", my_list)
else:
    print("Value not found in list")

#9
values = []
print("Enter 20 integers:")
for i in range(20):
    val = int(input(f"Enter element {i + 1}: "))
    values.append(val)

print("\nList:", values)

# a) Count occurrences and indices of elements
checked = []
print("\n--- Element Frequencies & Indices ---")
for i in range(len(values)):
    item = values[i]
    if item not in checked:
        checked.append(item)
        indices = []
        for j in range(len(values)):
            if values[j] == item:
                indices.append(j)
        print(f"Element {item}: Count = {len(indices)}, Indices = {indices}")

# b) Count even and odd values
even_count = 0
odd_count = 0
for x in values:
    if x % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("\nTotal Even numbers:", even_count)
print("Total Odd numbers:", odd_count)

# c) Count positive and negative values
pos_count = 0
neg_count = 0
for x in values:
    if x > 0:
        pos_count += 1
    elif x < 0:
        neg_count += 1
print("\nTotal Positive numbers:", pos_count)
print("Total Negative numbers:", neg_count)

#10
my_list = []
print("Enter 10 integers:")
for i in range(10):
    val = int(input(f"Enter number {i + 1}: "))
    my_list.append(val)

# a) Ascending using sorted()
asc_list = sorted(my_list)
print("\nAscending order (using sorted()):", asc_list)

# b) Descending using sort()
my_list.sort(reverse=True)
print("Descending order (using sort()):", my_list)

# c) Display length
print("Length of list:", len(my_list))

#11
list1 = input("Enter elements of first list separated by space: ").split()
list2 = input("Enter elements of second list separated by space: ").split()

merged_list = list1 + list2
print("Merged list:", merged_list)

#12
phrase = input("Enter a phrase: ")
words = phrase.split()

acronym = ""
for word in words:
    acronym += word[0].upper()

print("Acronym:", acronym)

#13
month_abbr = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

month_num = int(input("Enter month number (1-12): "))

if 1 <= month_num <= 12:
    print("Abbreviation:", month_abbr[month_num - 1])
else:
    print("Invalid month number! Enter between 1 and 12.")

# Dictionary
#1
my_dict = {0: 10, 1: 20}
print("Original dictionary:", my_dict)

my_dict[2] = 30

print("Updated dictionary:", my_dict)

#2
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

new_dict = {}
new_dict.update(dic1)
new_dict.update(dic2)
new_dict.update(dic3)

print("Concatenated dictionary:", new_dict)

#3
student = {"name": "Aman", "age": 20, "city": "Pune"}

key_to_check = input("Enter key to search: ")

if key_to_check in student:
    print(f"Key '{key_to_check}' exists in the dictionary with value: {student[key_to_check]}")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary")

#4
sample_dict = {"a": 100, "b": 200, "c": 300}

# Keys alone
print("Keys Alone")
for key in sample_dict:
    print(key)

# Values alone
print("\n Values Alone")
for key in sample_dict:
    print(sample_dict[key])

# Both keys and values
print("\n Both Keys and Values ")
for key, value in sample_dict.items():
    print(key, ":", value)

#5
square_dict = {}

for num in range(1, 16):
    square_dict[num] = num * num

print("Dictionary of squares (1 to 15):")
print(square_dict)

#6
my_dict = {"item1": 50, "item2": 150, "item3": 200}

total_sum = 0
for val in my_dict.values():
    total_sum += val

print("Dictionary:", my_dict)
print("Sum of all values:", total_sum)

#7
# Initial dictionary with 5 elements
my_dict = {
    "name": "Rohan",
    "roll_no": 101,
    "course": "B.Tech",
    "year": "2nd",
    "city": "Mumbai"
}
print("Original Student Info:", my_dict)

# Add student information
my_dict["phone"] = "9876543210"
print("\nAfter Adding Phone:", my_dict)

# Delete student information
del my_dict["city"]
print("\nAfter Deleting City:", my_dict)

# Display student information clearly
print("\n Final Student Details")
for key, value in my_dict.items():
    print(f"{key}: {value}")

#8
list1 = ['name', 'panel', 'rollno']
list2 = ['ABC', 'B', 34]

my_dict = {}
for i in range(len(list1)):
    my_dict[list1[i]] = list2[i]

print("Created Dictionary:", my_dict)

#9
sample_dict = {"name": "Priya", "age": 21, "branch": "CSE"}

keys_list = list(sample_dict.keys())
values_list = list(sample_dict.values())

print("List of Keys:", keys_list)
print("List of Values:", values_list)

#10
mydict = {'marks1': 23, 'marks2': 123, 'marks3': 43, 'marks4': 13, 'marks5': 39}

total = 0
count = 0

for val in mydict.values():
    total += val
    count += 1

mean = total / count
print("Mean of all values:", mean)

#11
my_dict = {'name': 'ABC', 'panel': 'B', 'rollno': 34, 'marks': [65, 87, 67, 94]}

sorted_keys = sorted(my_dict)
print("Sorted keys:", sorted_keys)

print("\nDictionary items sorted by key:")
for key in sorted_keys:
    print(f"{key}: {my_dict[key]}")

#Tuples
#1
my_tuple = (10, 20, 30, 40, 50, 60, 70, 80)
print("Tuple:", my_tuple)

fourth_from_first = my_tuple[3]

fourth_from_last = my_tuple[-4]

print("4th element from first:", fourth_from_first)
print("4th element from last:", fourth_from_last)

#2
numbers = (5, 10, 15, 20, 25)

target = int(input("Enter number to search: "))

if target in numbers:
    print(target, "exists in the tuple")
else:
    print(target, "does not exist in the tuple")

#3
my_list = [10, 20, 30, 40, 50]

# Using tuple() constructor
my_tuple = tuple(my_list)

print("Original list:", my_list)
print("Converted tuple:", my_tuple)

#4
fruits = ("apple", "banana", "cherry", "mango")
print("Tuple:", fruits)

item = input("Enter item to find its index: ")

if item in fruits:
    index_pos = fruits.index(item)
    print("Index of", item, "is:", index_pos)
else:
    print(item, "is not found in the tuple")

#5
sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_list = []

for t in sample_list:
    updated_tuple = t[:-1] + (100,)
    new_list.append(updated_tuple)

print("Original list:", sample_list)
print("Updated list:", new_list)

#Set
#1
my_set = {10, 20, 30, 40, 50}
print("Original set:", my_set)

item = int(input("Enter item to remove: "))

my_set.discard(item)

print("Set after removal:", my_set)

#2
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

result = set1.intersection(set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Intersection:", result)

#3
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.union(set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", result)

#4
numbers = {45, 12, 89, 3, 76, 24}
print("Set:", numbers)

maximum = max(numbers)
minimum = min(numbers)

print("Maximum value:", maximum)
print("Minimum value:", minimum)

#String
#1
text = input("Enter a string: ")

upper_count = 0
lower_count = 0

for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print("Uppercase letters count:", upper_count)
print("Lowercase letters count:", lower_count)

#2
text = input("Enter a string: ")

reversed_text = text[::-1]

if text == reversed_text:
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")


#3
text = input("Enter a string (length >= 2): ")

first_two = text[:2]
n = len(text)

result = first_two * n
print("Output:", result)

#4
text = input("Enter a string: ")

if len(text) > 0 and text[0] == 'x':
    text = text[1:]

if len(text) > 0 and text[-1] == 'x':
    text = text[:-1]

print("Output:", text)

#5
text = input("Enter a string: ")
n = int(input("Enter integer n: "))

# Extract last n characters
last_n = text[-n:] if n > 0 else ""

result = last_n * n
print("Output:", result)

#REGEX
#1
import re

pattern = r"^[bh][aiu]t$"

words = ["bat", "bit", "but", "hat", "hit", "hut", "cat", "bet"]
for word in words:
    if re.match(pattern, word):
        print(f"'{word}' matches the pattern")
    else:
        print(f"'{word}' does not match")

#2
import re

pattern = r"^[A-Za-z]+ [A-Za-z]+$"

test_names = ["Rahul Sharma", "John Doe", "Alice", "Dr. John Watson"]
for name in test_names:
    if re.match(pattern, name):
        print(f"'{name}' is a valid pair of words")
    else:
        print(f"'{name}' is not a valid pair")

#3
import re

pattern = r"^[A-Za-z]+, [A-Za-z]$"

test_entries = ["Sharma, R", "Watson, J", "Doe, John", "Smith,"]
for entry in test_entries:
    if re.match(pattern, entry):
        print(f"'{entry}' matches (Last Name, First Initial)")
    else:
        print(f"'{entry}' does not match")

#NUMPY
#1
import numpy as np

arr = np.full((3, 3), True)
print(arr)

#2
import numpy as np

arr = np.linspace(5, 50, 10)
print(arr)

#9
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

dot_prod = np.dot(arr1, arr2)
print("Dot Product:", dot_prod)

#8
import numpy as np

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([2, 4, 5, 8])

print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)