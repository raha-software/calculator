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
        for i in range(len(history)): # To print the numbered history
            print(f" {i+1}. {history[i]}")

history = []
box_number = None
pending_number = None # if operator wasn't character ,I used this variable.

while True:
    # If the operator is a number,  we use that number as the first operand;
    # essentially, we go back to the beginning of the sequence—first number,
    # then operator, then second number.
    if pending_number is not None:
        num_1 = pending_number
        pending_number = None#And now, we clear this variable again.
    elif box_number == None:    
         num_1 = input("Please enter a number!") 
    else:
        num_1 = box_number
        
    if num_1 == "h" or num_1 == "H":
        show_history()
        continue  

    if num_1 == "q" or num_1 == "Q":
        print("Goodbye")
        break
    
    if num_1 == "delete":
        if len(history) == 0:
            print("History is empty")
        else:
            show_history()
            while True:
                num = input("Which number do you want to delete?")
                try:
                    index = int(num)
                except ValueError: 
                    print("Input is invalid. Just number.")
                    continue

                if 1 <= index <= len(history):
                    history.pop(index - 1)
                    print(f"Item number {index} deleted.")
                    break
                else:
                    print("This number doesn't exist! Please try again.")
            continue 

    if num_1 == "c" or num_1 == "C": 
        history.clear()
        box_number = None 
        print("History deleted!")
        continue

    operator = input("What operator do you want?")
    try:
        float(operator)
        is_number = True
    except ValueError:
        is_number = False
        
    if is_number:
        pending_number = operator
        box_number = None # We clear this variable so that the program uses the number from the previous line.
        continue # It goes back to the beginning of the loop until what we wanted is done.

    if operator == "q" or operator == "Q":
        print("Goodbye")
        break

    if operator == "h" or operator == "H":
        show_history()
        continue

    if operator == "delete":
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
            continue 

    if operator == "c" or operator == "C":
        history.clear()
        box_number = None
        print("History deleted!")
        continue

    num_2 = input("Please enter another number!") 
    if num_2 == "q" or num_2 == "Q":
        print("Goodbye")
        break

    if num_2 == "h" or num_2 == "H":
        show_history()
        continue
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

            with open("E:/PythonProjects/file.txt", "a") as file:
                file.write(f"{con_total}\n")

    except ValueError:
            print("Entry is invalid!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
 

