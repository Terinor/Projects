list_numbers = ['065-875-94-11', '(81)8765347', '(65)765-89-77', '657658976', '8867658976']

def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    JP = []
    SG = []
    TW = []
    UA = []
    sanitized_numbers = list(map(sanitize_phone_number, list_phones))
        
    print (sanitized_numbers)

    for phone in sanitized_numbers:
        if phone.startswith("81"):
            JP.append(phone)
        elif phone.startswith("65"):
            SG.append(phone)
        elif phone.startswith("886"):
            TW.append(phone)
        else:
            UA.append(phone)
    numbers_for_countries = {'UA': UA, 
                             'JP': JP, 
                             'SG': SG, 
                             'TW': TW}
    
    return numbers_for_countries

print (get_phone_numbers_for_countries(list_numbers))