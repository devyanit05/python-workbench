# ------------------------------------------------------------------------
# Input and Output
# ------------------------------------------------------------------------

print('Hello')
print('Hello', 'Python', 3)

greeting = 'Good morning,'
name = 'Devyani'

formatted_message = '{} {}. Welcome!'.format(greeting, name)
print(formatted_message)

formatted_message_f = f'{greeting} {name.upper()}. Welcome!'
print(formatted_message_f)

print(f'{name} works at Regnology.')

# input() always returns a string — cast it if you need a number
# name = input('Enter your name: ')
# print(f'Hello, {name}')
