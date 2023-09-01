def is_valid_pin_codes(pin_codes):
    
    if not pin_codes:
        return False
    right_calls = 0
    for pin in pin_codes:
        if isinstance(pin, str) and str.isnumeric(pin) and len(pin_codes) == len(set(pin_codes)) and len(pin) == 4:
            right_calls += 1
    if right_calls == len(pin_codes):
        return True
    else:
        return False

print(is_valid_pin_codes(['1101', '9034', '0011', '1101']))    
print(is_valid_pin_codes(['1101', '9034', '0011']))