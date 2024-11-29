# If else statement
# 1
user_input = int(input("Enter your age: "))

if user_input >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# 2
day = input("Enter a day here.. ").lower()

if day == "sunday":
    print("You can play PUBG on your phone")
else:
    print("You can't play PUBG on your phone today")
    print("Today is working Day")

# 3
user = input("Plz enter day here: ").lower()

if user == "sunday":
    print("You can go to shopping") 
else:
    print("You will do online shopping.")

# 4
userInput = input("Plz enter day here: ").lower()

if userInput == "thursday":
    print("You will hang out with friends.") 
else:
    print("You will watch a movie at home")

# 6

user_input = input("Plz enter day here: ").lower()

if user_input == "tuesday":
    print("You will go Gym") 
else:
    print("You will practice yoga")