isDay =  input("Plz enter a day: ").lower()
isSunny = True

if isDay == "monday":
    print("I will do coding.")

elif isDay == "tuesday":
    print("I will study Python.")

elif isDay == "wednesday":
    print("I will practice problem-solving.")

elif isDay == "thursday":
    print("I will work on my project.")
    
elif isDay == "friday":
    print("I will learn new programming concepts.")
    
elif isDay == "saturday":
    print("I will revise everything I learned.")

elif isDay == "sunday" and isSunny:
    print("I will take a break and relax & go to eat IceCream")
else:
    print("Invalid day entered!")