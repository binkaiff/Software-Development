total = 0
count = 0
score = int(input("Enter score (Enter -9 to end): "))
while score != -9:
    total += score
    count += 1
    score = int(input("Enter score (Enter -9 to end): "))
if count > 0:
    average = float(total) / count
    print("Class average is", average)
else:
    print("No scores were entered.")