# Comprehension Assignment: Lambda Functions and Functional Programming
# Name: ______________________
#
# Topics covered:
# lambda, map(), filter(), sorted()

# ---------------------------------------------------------
# 1. Lambda Functions
# ---------------------------------------------------------

# Double a given number
double = lambda x: x * 2
print("1. Double:", double(10))

# Find the remainder when one number is divided by another
remainder = lambda a, b: a % b
print("2. Remainder:", remainder(17, 5))

# Check whether a number is divisible by 5
divisible_by_5 = lambda x: x % 5 == 0
print("3. Divisible by 5:", divisible_by_5(25))

# Find the smaller of two numbers
smaller = lambda a, b: a if a < b else b
print("4. Smaller number:", smaller(15, 8))

# Convert Celsius to Fahrenheit
celsius_to_fahrenheit = lambda c: (c * 9 / 5) + 32
print("5. Fahrenheit:", celsius_to_fahrenheit(25))


# ---------------------------------------------------------
# 2. map() and lambda
# ---------------------------------------------------------

# Add 5 to every number
numbers = [10, 20, 30, 40, 50]

add_5 = list(map(lambda x: x + 5, numbers))

print("\n6. Add 5 to every number:")
print(add_5)


# Convert all names to uppercase
names = ["aparna", "ravi", "priya", "kiran"]

uppercase_names = list(map(lambda name: name.upper(), names))

print("\n7. Names in uppercase:")
print(uppercase_names)


# ---------------------------------------------------------
# 3. filter() and lambda
# ---------------------------------------------------------

# Find ages 18 and above
ages = [12, 18, 25, 15, 30, 10, 22]

adult_ages = list(filter(lambda age: age >= 18, ages))

print("\n8. Ages 18 and above:")
print(adult_ages)


# Find names having more than 4 characters
names = ["Ram", "Aparna", "Ravi", "Priyanka", "Sai"]

long_names = list(filter(lambda name: len(name) > 4, names))

print("\n9. Names with more than 4 characters:")
print(long_names)


# ---------------------------------------------------------
# 4. sorted() and lambda
# ---------------------------------------------------------

# Sort students based on marks from highest to lowest
students = [
    ("Aparna", 85),
    ("Ravi", 72),
    ("Priya", 95),
    ("Kiran", 65)
]

sorted_students = sorted(students, key=lambda student: student[1], reverse=True)

print("\n10. Students sorted by marks (highest to lowest):")
for student in sorted_students:
    print(student)
