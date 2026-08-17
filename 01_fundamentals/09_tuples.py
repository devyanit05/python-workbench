# ------------------------------------------------------------------------
# Tuples
# ------------------------------------------------------------------------
# Lists are mutable. Tuples are immutable. Tuples are faster than lists,
# can be used as dictionary keys, and can return multiple values from a function.

list1 = [1, 2, 3, 4, 5]
tuple1 = (1, 2, 3, 4, 5)
list2 = list1
tuple2 = tuple1

print(list1)
print(list2)
print(tuple1)
print(tuple2)

list1[0] = 10
print(list1)
print(list2)  # list2 changes too because it is a reference to list1

# tuple1[0] = 10  # TypeError: tuples are immutable
print(tuple1)
print(tuple2)

empty_tuple = ()
empty_tuple = tuple()

# Unpacking
coordinates = (10, 20)
x, y = coordinates
print(x, y)
