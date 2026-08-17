# ------------------------------------------------------------------------
# List Comprehensions
# ------------------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

squares = [n * n for n in numbers]
print(squares)

evens = [n for n in numbers if n % 2 == 0]
print(evens)

courses = ['Python', 'Java', 'C++', 'JavaScript']
upper_courses = [course.upper() for course in courses]
print(upper_courses)
