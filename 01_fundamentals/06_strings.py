# ------------------------------------------------------------------------
# Strings
# ------------------------------------------------------------------------

message = 'Devyaniiiiiiiiiii'
multiline_message = '''This
It can span multiple lines.'''

print(message[0])
print(message[3])
print(message[-6])
print(message[0:6])
print(multiline_message[4:10])
print(multiline_message[4:15:2])  # every second character
print(len(message))
print(message[::-1])              # reverse with slicing

greeting = 'Good morning, '
name = 'Devyani'
print(greeting + name)
print(greeting * 2)

# The from-scratch length and reverse versions live in
# 09_interview_questions/07_string_length.py and 06_reverse_string.py.
