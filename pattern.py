rows = 9 #indexes the number of rows needed
for i in range(rows):
    if i < 5: #calculates i until i==5
        print("*" * (i+1))
    else: # calculates i above 5 
        i = rows - i 
        print("*" * i)
