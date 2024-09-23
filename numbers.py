#start
#ask user to input 3 numbers
#add the inputs together
#deduct the second number from the first
#multiply the third number by the first
#use the sum from all 3 numbers
#divide the sum by the third number
num_1 = int(input("please enter a whole number "))
num_2 = int(input("please enter a second whole number "))
num_3 = int(input("please enter your third and last whole number "))

addition = int(num_1 + num_2 + num_3) # adds each input in sequence
print("the sum of your numbers is: ")
print(addition) #prints the sum of inputs

subtraction = int(num_1 - num_2) # deducts number 2 from number 1
print("Your first number minus the second number is: ")
print(subtraction) # prints result

multiplication = int(num_3 * num_1) #multiplies numbers 3 with 1
print("your third number multiplied by the first number is: ")
print(multiplication) # prints result

sum_division = float(addition / num_3) #divides the total sum of numbers with third number
print("the total sum of all your numbers divided by the third number is: ") 
print(sum_division) # prints the result
