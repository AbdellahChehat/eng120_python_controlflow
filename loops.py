# list_data = [1, 2, 3, 4, 5]
#
# for number in list_data:
#     if number == 3:
#         print(number)
#
#     elif number > 3:
#         print ("You have passed 3")
#
#     else:
#         print("too early")



# print(list_data)
# print(list_data[0])

# Create a dictionary student_data
# iterate through the dict
# using control flow - if elif - else and for the loop print all the keys
# print all the values
# print key with matching value = "Abdella"

student_data = {
    "Student_name": "Abdellah",
    "stream":"devops",
    "completed_lesson": 4,
    "completed_lesson_names": ["tuples", "lists", "strings"]

}

# iterate through the dict

for x, y in student_data.items():
  print(x, y)

# using control flow - if elif - else and for the loop print all the keys
for keys in student_data:
    print(keys)

# print all the values

for value in student_data:
    print(student_data[value])

# print key with matching value = "Abdellah"

for value in student_data:
    print(student_data[value("studnet_name")])