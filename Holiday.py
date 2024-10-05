num_nights = 8
rental_days = 7

def hotel_cost(x):
    y = x  * num_nights
    return y
res_hotel = hotel_cost(100)
print("cost of hotel is: " ,res_hotel,"£")

city_flight = "malta", "mauritius", "copenhagen"

def plane_cost(x):
    if x == "malta":
        y = 2 * 90
    elif x == "mauritius":
        y = 2 * 350
    elif x == "copenhagen":
        y = 2 * 110
    return y
result_flight = plane_cost("mauritius")
print("cost of a flights are: " ,result_flight,"£")

def car_rental(x):
    y = x * rental_days
    return y
result_car = car_rental(50) #result_of_function variable = function(argument)
print("Cost of car rental is: " ,result_car,"£")

def holiday_cost(a, b, c):
    total = a + b + c
    return (total)
result_holiday = (result_flight) + (result_car) + (res_hotel)
print("Total cost of your holiday is: " ,result_holiday,"£")