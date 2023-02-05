my_dict = {
    'name':'Romeo',
    'last_name':'Santana',
    'age': 33,
    'address':'Insurgentes #100',
    'lenguages':('Python', 'JavaScript', 'HTML')
    }

for key in my_dict.keys():
    print(key)

print()

for value in my_dict.values():
    print(value)

print()

for key, value in my_dict.items():
    print(f'{key} -> {value}')