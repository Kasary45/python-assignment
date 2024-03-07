def cel_to_fer():
    temp=int(input("Enter the Temperature in celcius to convert into fer:"))
    fahrenheit = (temp* 1.8) + 32
    print(f"temperature in fahrenheit is {fahrenheit}")
cel_to_fer()

def fer_to_cel():
    temp=int(input("Enter the Temperature in fahrenheit  to convert into cel:"))
    celecious = ((temp-32)*(5//9))
    print(f"temperature in celecious is {celecious}")
fer_to_cel()




