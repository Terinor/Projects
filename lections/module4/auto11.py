def is_valid_password(password):
    upper = False
    lower = False
    numeric = False
        
    if len(password) != 8:
        return False
    for i in password:
        if i.isupper():
            upper = True
        if i.islower():
            lower = True
        if i.isnumeric():
            numeric = True
    return (upper and lower and numeric)

print(is_valid_password("12345"))
print(is_valid_password("NW;^Li"))
print(is_valid_password("s,7O>SS7"))