# Assignment One for Python - Arush Mahajan (Div:13)
# List

my_list = [30, 10, 50, 20, 40]

print("Original List:", my_list)

my_list.append(60)
print("After append:", my_list)

my_list.insert(2, 25)
print("After insert:", my_list)

my_list.remove(25)
print("After remove:", my_list)

my_list.pop()
print("After pop:", my_list)

my_list.sort()
print("After sort:", my_list)


# Tuple
mytuple = (10, 20, 30, 20, 40)
print("\nOriginal Tuple:", mytuple)
print("Count of 20:", mytuple.count(20))
print("Index of 30:", mytuple.index(30))
print("Length of Tuple:", len(mytuple))
print("Maximum value:", max(mytuple))
print("Minimum value:", min(mytuple))


# Dictionary
student = {
    "name": "Anil",
    "age": 18,
    "branch": "CSE"
}
print("\nOriginal Dictionary:", student)

student["college"] = "MIT-WPU"
print("After adding element:", student)

student.update({"age": 20})
print("After update:", student)

print("Name:", student.get("name"))
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

student.pop("age")
print("After removing age:", student)