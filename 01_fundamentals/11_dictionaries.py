# ------------------------------------------------------------------------
# Dictionaries
# ------------------------------------------------------------------------
# Dictionaries are collections of key-value pairs.

dictionary = {
    'name': 'Devyani',
    'age': 25,
    'city': 'New York',
    'is_student': False,
    'skills': ['Python', 'Java', 'C++', 'JavaScript'],
    'worksAt': 'Regnology',
    'address': {
        'street': '123 Main St',
        'city': 'New York',
        'state': 'NY',
        'zip': '10001',
    },
    'phone_numbers': ['123-456-7890', '987-654-3210'],
    'email': 'devyani@example.com',
    1: 'true',
}

print(dictionary)
print(dictionary['name'])
print(dictionary.get('age'))
print(dictionary.get('gender', 'Not specified'))

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

dictionary['age'] = 26
print(dictionary)

dictionary.pop('city')
print(dictionary)

dictionary.popitem()
print(dictionary)

dictionary.update({'city': 'Los Angeles', 'is_student': True})
print(dictionary)

for key, value in dictionary.items():
    print(f'Key: {key}, Value: {value}')

for key in dictionary:
    print(key)

for value in dictionary.values():
    print(value)

empty_dict = {}
empty_dict = dict()
