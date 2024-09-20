# declare a series of variables
#one float two integers and one string
# cast float into a string
# cast first integer into a float
# cast second integer into a string
# cast string into an integer

num1 = 99.23
num2=23
num3=150
string1 = "100"

new_float = int(num1) #changing the variable into an integer and a whole number
print(new_float) #prints 99

new_float2 = float(num2) #Changes the integer to a float i.e a decimal number
print(new_float2) #prints out 23.0

new_str = str(num3) # changes the variable so you can't use it to calculate with
print(new_str) #prints 150 as a string

new_int = int(string1) #changes from a string to an integer, to enable calculation
print(new_int) #100 as an integer

#result is a list as below
#99
#23.0
#150
#100
