result = None
operand = None
operator = None
wait_for_number = True
action = ['+', '-', '*', '/', '=']
while True:
    user_input = input(">>> ")
    if user_input == '=':
        break
    if wait_for_number:
        try:
            operand = float(user_input)
        except ValueError:
            print("It isn't numeric number! Try again!")
            continue
        wait_for_number = False
        if not result:
            result = operand
        if operator == "=":
            print(result)
            break
        else:
            if operator == "+":
                result += operand
            elif operator == "-":
                result -= operand
            elif operator == "*":
                result *= operand
            elif operator == "/":
                try:
                    result /= operand
                except ZeroDivisionError:
                    print("Ділення на 0")
                    continue
    else:
        if user_input in action:
            operator = user_input
        else:
            operator = None

        if not operator:
            print("Not operator")
        else:
            wait_for_number = True








