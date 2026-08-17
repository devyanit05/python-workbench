# ------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------

def greet(name):
    return f'Hello, {name}'

print(greet('Devyani'))

def add(a, b=0):
    return a + b

print(add(2, 3))
print(add(2))

def classify(num):
    if num > 0:
        return 'Positive'
    elif num < 0:
        return 'Negative'
    return 'Zero'

print(classify(-7))

# Recursion: a function that calls itself.
# The interview Fibonacci version lives in 09_interview_questions/02_fibonacci.py.
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print([fibonacci(i) for i in range(10)])
