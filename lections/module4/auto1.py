def amount_payment(*payment):
    sum = 0
    for pay in payment:
        if pay >= 0:
            sum += pay
    return sum
print (amount_payment(1, -3, 4))