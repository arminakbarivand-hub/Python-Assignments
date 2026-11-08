name = input("enter your name: ")
last_name = input("enter your lastname: ")
age = input("enter your age: ")

print("Your first name is "+ name +" , your last name is "+ last_name +".")
print("So your full name is "+ name +" " + last_name + ".")
print("Your age is",age,"years old.")

print(f"Your first name is {name} , your last name is {last_name}.")
print(f"So your full name is {name} {last_name}.")
print(f"Your age is {age} years old.")

print("Your first name is {} , your last name is {}.".format(name,last_name))
print("So your full name is {} {}.".format(name,last_name))
print("Your age is {} years old.".format(age))