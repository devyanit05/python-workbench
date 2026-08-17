# ------------------------------------------------------------------------
# Lists
# ------------------------------------------------------------------------
# Lists are mutable, ordered collections.

courses = ['Python', 'Java', 'C++', 'JavaScript']
courses_2 = ['Go', 'Rust', 'Kotlin']

print(courses)
print(courses[0])    # first element
print(courses[-1])   # last element
print(courses[0:2])  # first two elements
print(courses[::2])  # every second element
print(courses[::-1]) # reverse the list
print(len(courses))

courses.append('C#')
print(courses)

courses.insert(1, 'Go')
print(courses)

courses.extend(courses_2)
print(courses)

courses.remove('Java')
print(courses)

print(courses.pop())
print(courses)

courses.pop(1)
print(courses)

courses.sort()
print(courses)

courses.sort(reverse=True)
print(courses)

courses.reverse()
print(courses)

sorted_courses = sorted(courses)
print(sorted_courses)

print(min(courses))
print(max(courses))
print(courses.index('Python'))
print('Python' in courses)
print('Java' not in courses)

course_str = ', '.join(courses)
print(course_str)
print(course_str.split(', '))

numbers = [10, 20, 30, 40]
average = sum(numbers) / len(numbers)
print(average)

empty_list = []
empty_list = list()

courses.clear()
print(courses)
