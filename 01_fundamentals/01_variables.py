# ------------------------------------------------------------------------
# Variables
# ------------------------------------------------------------------------

name = 'Devyani'
age = 25
is_student = False
works_at = 'Regnology'

print(name)
print(age)
print(is_student)
print(works_at)

# Multiple assignment
x, y, z = 1, 2, 3
print(x, y, z)

# Values can be overwritten
age = 26
print(age)

# Swap with tuple unpacking — Python does not need a temp variable.
# The arithmetic interview trick lives in 09_interview_questions/01_swap_numbers.py.
num1 = 100
num2 = 20
print(num1, num2)
num1, num2 = num2, num1
print(num1, num2)
