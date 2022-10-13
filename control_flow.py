#

#
# weather = "cold"
# # if it's cold:
# if weather == "cold" : #if true or false
#     print("wear a jacket")
# elif weather == "sunny" :
#     print("lets go to the beach")
#
# else:
#     print("No match found better luck next time")

     #rain mack

# else or elif
# Age restriction for movie ticket
# Create a condition for 18 & above
# Create 16 & above
# universal
# pg
# 12a
# 15 and above
# if nothing matched inform the user to enter age again
# user must not be allowed to anter age over 117 years

age = 18
age1 = 16
age2 = 12
age3 = 15

#Create a condition for 18 & above

print("Hello, Enter your age")
user_age = int(input("enter age"))
if user_age >= 18  <= 116:
    print("You are allowed to watch 18+ pg rated movies ")

elif user_age != 18 :
    print("You are not able to watch 18 + pg rated movies")

# Create 16 & above
if user_age >= 16 <= 116:
    print("You are allowed to watch 16+ pg rated movies ")

elif user_age != 16:
    print("You are not able to watch 16+ this movie")

# Create 15 and above
if user_age >= 15 <= 116:
    print("You are allowed to watch 15+ rated movies ")

elif user_age != 15:
    print("You are not able to watch 15+ movie")

# Create 12 and above
if user_age >= 12 <= 116:
    print("You are allowed to watch 12a rated movies ")

elif user_age != 12:
    print("You are not able to watch 12a rated movies")

# user must not be allowed to anter age over 117 years

if user_age >= 177 :
    print("Enter age under 117 again in digits ")

else:
    print("Enter age in digits ")

