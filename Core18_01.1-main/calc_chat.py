result = None
operand = None
operator = None
wait_for_number = True

while True:
    while wait_for_number:
        try:
            input_value = input(">>> ")

            if input_value == "=":
                print("Результат:", result)
                exit()

            if input_value in ("+", "-", "*", "/"):
                if operator is not None or operand is None:
                    print(f"Помилка: Оператор {input_value} вже введений. Введіть число.")
                else:
                    operator = input_value
                    wait_for_number = False
            else:
                operand = float(input_value)
                wait_for_number = False

        except ValueError:
            print(f"Помилка: {input_value} не є числом. Спробуйте ще раз.")

    try:
        input_value = input("Введіть число: ")
        if input_value in ("+", "-", "*", "/"):
            print(f"Помилка: {input_value} не є числом. Спробуйте ще раз.")
        else:
            second_operand = float(input_value)

            if operator == "+":
                result = operand + second_operand
            elif operator == "-":
                result = operand - second_operand
            elif operator == "*":
                result = operand * second_operand
            elif operator == "/":
                result = operand / second_operand

            operand = result
            operator = None
            print("Проміжний результат:", result)
            wait_for_number = True

    except ValueError:
        print("Помилка: Введіть коректне число.")
