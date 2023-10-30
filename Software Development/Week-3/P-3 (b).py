int1 = int(input("Enter the first integer: "))
opp = input("Enter the operator (+, -, *): ")
int2 = int(input("Enter the second integer: "))

if opp == '+':
    output = int1 + int2
elif opp == '-':
    output = int1 - int2
elif opp == '*':
    output = int1 * int2
else:
    print("Invalid operator. Please enter +, -, or *.")
    exit()  # Exit the program if the operator is invalid

print("Expected Result is", output)
