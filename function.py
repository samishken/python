# Group of statements to perform a specific task
# def is_adult(age):
#     return age >= 16
# result = is_adult(14)
# print(result)

def convertGender(gender="unknown"):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper() == "F":
        return "Female"
    else:
        return f"Gender {gender} is unknown"
print(convertGender("F"))
print(convertGender("M"))
print(convertGender("f"))
print(convertGender("m"))
print(convertGender("Hello"))



# # Arguments
# def greet(name, age=-1):
#     print(f"Hello {name}, How are you?")
#     if age > 0:
#         print(f"I know your age = {age} ")
# greet("Teddy")  # For Teddy it's not going to print the default age because it's less than 0
# greet("Stevie", 22)


# def greet(name):
#     print(f"Hello {name} how are you?")
# greet("Teddy")
# greet("Stevie")


# def greet():
#     print("Hello how are you")
# greet()