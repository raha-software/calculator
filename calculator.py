def calculate(con_num_1, con_num_2, operator):
    if operator == "+":
        return con_num_1 + con_num_2
    elif operator =="-":
        return con_num_1 - con_num_2
    elif operator == "*":
        return con_num_1 * con_num_2
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
        for i in range(len(history)):# To print the numbered history
            print(f" {i+1}. {history[i]}")


history = []

while True:
    
    num_1 = input("Please enter one number!")
    if num_1 == "q" or num_1 == "Q":
        print("Goodbye")
        break
    if num_1 == "h" or num_1 == "H":
        show_history()
        continue

    if num_1 == "delete":
        if len(history) == 0:
            print("History is empty")
        else:
            show_history()
            while True:
                num = input("Which one number do you wanted to deleted ?")
                try:
                    index = int(num)
                except ValueError: 
                    print("Input is invalid . Just number .")
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
        print("History deleted!")
        continue
    num_2 = input("Please enter another number!")
    if num_2 == "q" or num_2 == "Q":
        print("Goodbye")
        break
    if num_2 == "h" or num_2 == "H":
        show_history()
        continue
    operator = input("What operator do you want ?")
    if operator == "q" or operator == "Q":
        print("Goodbye")
        break
    if operator == "h" or operator == "H":
        show_history()
        continue
    try:
        con_num_1 = float(num_1)
        con_num_2 = float(num_2)
        total = calculate(con_num_1, con_num_2, operator)
        if total is None:
            print("Operator is invalid")
        else:
            total = pretty(total)
            print(total)
            history.append(f"{pretty(con_num_1)} {operator} {pretty(con_num_2)} = {total}")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Entry is invalid.")
