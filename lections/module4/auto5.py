def lookup_key(data, value):
    keys = []
    for key, val in data.items():
        if val == value:
            keys.append(key)
    return keys

# Приклад використання
my_dict = {
    'a': 1,
    'b': 2,
    'c': 2,
    'd': 3,
    'e': 2
}

search_value = 2
result = lookup_key(my_dict, search_value)

if result:
    print(f"Keys with value {search_value}: {result}")
else:
    print(f"No keys found for value {search_value}")