# ------------------------------------------------------------------------
# Loops
# ------------------------------------------------------------------------

courses = ['Python', 'Java', 'C++', 'JavaScript']

for item in courses:
    print(item)

for item in courses:
    print(courses.index(item), item, item.upper())

for index, item in enumerate(courses):
    print(index, item)

for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

n = 10
total = sum(range(1, n + 1))
print(total)

count = 0
while count < 5:
    print(count)
    count += 1

# Fibonacci built with a loop — the interview version lives in
# 09_interview_questions/02_fibonacci.py.
sequence = [0, 1]
for _ in range(2, 10):
    sequence.append(sequence[-2] + sequence[-1])
print(sequence)
