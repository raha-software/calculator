def calculate(con_num_1, operator, con_num_2):
    if operator == "+":
        return con_num_1 + con_num_2
    elif operator == "-":
        return con_num_1 - con_num_2
    elif operator == "*":
        return con_num_1 * con_num_2
    elif operator == "**":
        return con_num_1 ** con_num_2
    elif operator == "/":
        return con_num_1 / con_num_2
    elif operator == "%":
        return con_num_1 % con_num_2
    else:
        return None 


def pretty(num):
    if num.is_integer():
        return int(num)
    return num 


def show_history():
    if len(history) == 0:
        print("History is empty")
    else:
        for i in range(len(history)):  # To print the numbered history
            print(f" {i+1}. {history[i]}")


def handle_commands(token):
    if token in ("h", "H"):
        show_history()
        return "continue"

    if token in ("q", "Q"):
        print("Goodbye")
        return "quit"
    
    if token in ("c", "C"):
        history.clear()
        print("history deleted!")
        return "continue"

    if token in ("delete", "DELETE"):
        if len(history) == 0:
            print("History is empty")
        else:
            show_history()
            while True:
                num = input("Which number do you want to delete?")
                try:
                    index = int(num)
                except ValueError: 
                    print("Input is invalid. Just a number.")
                    continue

                if 1 <= index <= len(history):
                    history.pop(index - 1)
                    print(f"Item number {index} deleted.")
                    break
                else:
                    print("This number doesn't exist! Please try again.")
                break
        return "continue"
    return "not_command"


history = []
box_number = None
pending_number = None # if operator wasn't character ,I used this variable.
exit_program = False

while True:
    # If the operator is a number,  we use that number as the first operand;
    # essentially, we go back to the beginning of the sequence—first number,
    # then operator, then second number.
    if pending_number is not None:
        num_1 = pending_number
        pending_number = None # And now, we clear this variable again.
    elif box_number == None:
        num_1 = input("Please enter a number!")
        result = handle_commands(num_1)
        if result == "continue":
            continue
        if result == "quit":
            break
    else:
        num_1 = box_number
    
    operator = input("What operator do you want?")
    result_2 = handle_commands(operator)
    if result_2 == "continue":
        continue
    
    if result_2 == "quit":
        break

    try:
        float(operator)
        is_number = True
    except ValueError:
        is_number = False

    if is_number:
        pending_number = operator
        box_number = None # We clear this variable so that the program uses the number from the previous line.
        continue # It goes back to the beginning of the loop until what we wanted is done.

    if pending_number != None:
        continue # Since this is outside the inner loop, it goes to the main loop first—specifically, to the point where it reads `pending_number` and sets the initial value.
    
    while True:
        num_2 = input("Please enter another number!") 
        result_3 = handle_commands(num_2)
        if result_3 == "continue":
            continue
        if result_3 == "quit":
            exit_program = True
            break
        break
    if exit_program:
        break

    try:
        con_num_1 = float(num_1)
        con_num_2 = float(num_2)
        total = calculate(con_num_1, operator, con_num_2)

        if total is None:
            print("Operator is invalid")
        else:
            total = pretty(total)
            box_number = total
            print(total)
            history.append(f"{pretty(con_num_1)} {operator} {pretty(con_num_2)} = {total}")
            con_total = str(total)
            try:
                with open("file.txt", "a") as file:
                    file.write(f"{con_total}\n")
            except OSError:
                print("Could not write to file")

    except ValueError:
            print("Entry is invalid!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
 

