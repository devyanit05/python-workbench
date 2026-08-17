# ------------------------------------------------------------------------
# Type Casting
# ------------------------------------------------------------------------

age_text = '25'
count = 10
pi = 3.14159
flag = 1

print(int(age_text))
print(float(count))
print(str(count))
print(int(pi))          # truncates toward zero
print(bool(flag))       # 0 is False, anything else is True
print(bool(0))
print(bool(''))
print(bool('Python'))

# Casting is common when reading input, which always returns a string
raw = '42'
print(int(raw) + 8)
