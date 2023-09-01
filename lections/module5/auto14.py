'''                                                                ['Ima.Fool@iana.org', 'first_last@iana.org', 'first.middle.last@iana.or', 'abc111@test.com.net']. 
Очікувалося, що функція find_all_emails при отриманні параметра     'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net' 
поверне наступний список                                        [   'Ima.Fool@iana.org', 'Fool@iana.org', 'first_last@iana.org', 'first.middle.last@iana.or', 'abc111@test.com']'''

import re


def find_all_emails(text):
    result = re.findall(r'\D\B[A-Za-z0-9.-_]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}', text)
    return result

adreses = 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'

print (find_all_emails(adreses))

# s = "I bought 77 nuts for 6$ and 110 bolts for 3$."

# print(re.findall("(\d){2}", s))  # ['0']
# print(re.findall("[\d]{2}", s))  # ['110']