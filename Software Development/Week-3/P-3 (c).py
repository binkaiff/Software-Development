cost = float(input("Enter the cost of the meal: "))
sat = int(input("Enter 1 = Totally satisfied, 2 = Satisfied, 3 = Dissatisfied: "))

if sat == 1:
    tip = cost * 0.2
elif sat == 2:
    tip = cost * 0.15
elif sat == 3:
    tip = cost * 0.1
else:
    print("Invalid input. Please enter 1, 2, or 3 for satisfaction level.")
    exit()  # Exit the program if the input is invalid

print("Tip amount is", tip)
