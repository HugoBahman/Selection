#Hugo
#Selection - Development Excercise 2
#03/10/14

print("This program takes the Centigrade temperature of water and tells you what state it is in.")
water_temp = float(input("Please enter the temperature of the water: "))
if water_temp < 0:
    print("The water is freezing.")
elif water_temp > 0 and water_temp < 100:
    print("The water is normal.")
else:
    print("The water is boiling.")
