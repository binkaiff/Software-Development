mark = int(input('Please enter the mark: '))

if mark < 0 or mark > 100:
    print("Invalid mark")
elif mark >= 70:
    print("Exceptional result!")
elif mark >= 40:
    print("Satisfactory result!")
else:
    print("You have failed.")
