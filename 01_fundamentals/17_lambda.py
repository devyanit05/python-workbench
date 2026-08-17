# ------------------------------------------------------------------------
# Lambda
# ------------------------------------------------------------------------
# A lambda is a small anonymous function: lambda arguments: expression

add = lambda a, b: a + b
print(add(2, 3))

square = lambda n: n * n
print(square(4))

courses = ['Python', 'Java', 'C++', 'JavaScript']
print(sorted(courses, key=lambda course: len(course)))
