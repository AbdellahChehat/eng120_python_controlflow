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
if user_age >= 18 :
    print("You are allowed to watch 18+ pg rated movies ")

elif user_age != 18 :
    print("You are not able to watch 18 + pg rated movies")

# Create 16 & above
if user_age >= 16 :
    print("You are allowed to watch 16+ pg rated movies ")

elif user_age != 16:
    print("You are not able to watch this movie")

else:
    print("Enter age in digits ")

