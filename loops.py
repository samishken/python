# loop through list or set
names = ["Ahmed", "Annah", "James", "Teddy", "Bob"]  # this could also be Set

# for loop
for name in names:
    print(name)

# loop through dictionary
person = {
    "name": "Jamal",
    "age": 20,
    "address": "USA"
}

# for key in person:
#     print(f"key:{key} value:{person[key]}")

print(person.items())
print(" ")
for key, value in person.items():
    print(f"key:{key} value:{value}")