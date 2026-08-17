# ------------------------------------------------------------------------
# random module
# ------------------------------------------------------------------------

import random

print(random.random())           # float from 0.0 to 1.0
print(random.randint(1, 10))     # integer from 1 to 10 inclusive
print(random.randrange(0, 10, 2))
print(random.choice(['Python', 'Java', 'C++']))
print(random.uniform(1.5, 5.5))

courses = ['Python', 'Java', 'C++', 'JavaScript']
random.shuffle(courses)
print(courses)

print(random.sample(range(1, 50), 5))
