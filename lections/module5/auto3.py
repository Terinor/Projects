def sanitize_phone_number(phone):
    control_chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    norm_number = "".join([char for char in phone if char in control_chars])
    return norm_number

print (sanitize_phone_number("    +38(050)123-32-34"))