temp = float(input("Enter the temperature: "))
con = int(input("Enter 1 to convert Temperature to Fahrenheit or 2 to convert temperature to Celsius: "))

if con == 1:
    t_f = (temp * 1.8) + 32
    print("Temperature in Fahrenheit:", t_f)
elif con == 2:
    t_c = (temp - 32) / 1.8
    print("Temperature in Celsius:", t_c)
else:
    print("Invalid input. Please enter 1 or 2 to choose the conversion type.")
