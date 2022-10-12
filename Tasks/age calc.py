import datetime

birthday = input("enter your birth day: (format dd/mm/yyyy)")
age = datetime.datetime.now().date() - birthday
print(f'Your Age is, {age} years old')



user_prompt = True

while user_prompt:
    year_of_birth = input("please enter your year of birth")
    if age.isdigit():
        user_prompt= False

    else:
        print("please enter your age in digits only")


print(f'your age is {age}')

#calculate their age - year of birth etc.