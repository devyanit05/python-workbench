# ------------------------------------------------------------------------
# Operators
# ------------------------------------------------------------------------

# Arithmetic
a = 10
b = 3
print('Add:', a + b)
print('Subtract:', a - b)
print('Multiply:', a * b)
print('Divide:', a / b)
print('Floor Divide:', a // b)
print('Modulus:', a % b)
print('Exponentiation:', a ** b)
print('Power:', pow(a, b))
print('Absolute:', abs(-a))
print('Round to 2 places:', round(3.14159, 2))
print('Round to integer:', round(3.14159))
print('Round to nearest 10:', round(32.14159, -1))

# Comparison
a = 10
b = 20
print('Equal:', a == b)
print('Not Equal:', a != b)
print('Greater Than:', a > b)
print('Less Than:', a < b)
print('Greater Than or Equal To:', a >= b)
print('Less Than or Equal To:', a <= b)

# Logical
a = True
b = False
print('And:', a and b)
print('Or:', a or b)
print('Not:', not a)

# Bitwise
a = 10  # 1010
b = 4   # 0100
print('Bitwise AND:', a & b)
print('Bitwise OR:', a | b)
print('Bitwise XOR:', a ^ b)
print('Bitwise NOT:', ~a)
print('Bitwise Left Shift:', a << 1)
print('Bitwise Right Shift:', a >> 1)

# Assignment
a = 10
b = 20
a += b  # a = a + b
print('Addition assignment:', a)
