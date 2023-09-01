result = None
operand = None
operator = None
wait_for_number = True
i = True
while True:

    while not wait_for_number:
        operator = input('>>> ')
        if operator in ('+', '-', '*', '/', '='):
            wait_for_number = True
            if operator == "=":
                print (f'Result: {result}')
                i = False
        else:
            print("It is not '+' or '-' or '/' or '*'or '='. Try again.")

    while wait_for_number:

        try:
            operand = float(input('>>> '))
            wait_for_number = False

        except ValueError:
            print("It is not a number. Try again.")

    if operator is None:
        result = operand
    elif operator == '+':
        result += operand
    elif operator == '-':
        result -= operand
    elif operator == '*':
        result *= operand
    elif operator == '/':
        result /= operand