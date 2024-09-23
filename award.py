#start
#ask user to input swimming time
#ask user to input cycling time
#ask user to input running time
#add the times together
#if total time is between 0-100
#reward honorary colours
#if total time is between 101-105 minutes
#reward honorary half colours
#if total time  Within 10 minutes of the  qualifying time
#reward honorary scroll
#if total time is more than 10 minutes from qualifying time
#reward is  nothing

swim_time = int(input("please enter your time for swimming "))
run_time = int(input("please enter your time for running "))
cycle_time = int(input("please enter your time for cycling ")) #takes input from user 

race_time = int(swim_time + run_time + cycle_time) #calculates total time
print("your race time is: ")
print(race_time)(" minutes"))

if race_time <= 100:
    print("congratulations! You win Honorary colours. Well done!")
elif (race_time >= 100) or (race_time <= 105):
    print("Congratulations! You win Honorary half colours")
elif (race_time >= 106) or (race_time <= 110):
    print("Well done, you have made it on to the Honorary scroll")
else:
    print("well done for completing the race today")