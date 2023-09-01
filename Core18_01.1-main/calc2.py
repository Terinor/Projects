result = None
operand = None
operator = None
wait_for_number = True

while True:
    input_value = (input('>>> '))
    if wait_for_number == True:
        try:
            operand = float(input_value)
            wait_for_number = False
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
                
        except ValueError:
            print("It is not a number. Try again.")

    else:

        operator = input_value
        if operator in ('+', '-', '*', '/', '='):
            wait_for_number = True
            if operator == "=":
                print (f'Result: {result}')
                break
        else:
            print("It is not '+' or '-' or '/' or '*'or '='. Try again.")