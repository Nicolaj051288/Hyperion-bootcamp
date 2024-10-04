num = 0
count = 0
total = 0

while True:
    num = int(input("Enter a number: "))
    count = count + 1
    total = total + num
    if num == 0:
        count = count - 1
    elif num == -1:
        count = count - 1
        total = total + 1
        break
print(f"You entered {count} numbers")
print(f"The sum of all your numbers is: {total}")
average = total / count
print(f"your average input was: {average}")