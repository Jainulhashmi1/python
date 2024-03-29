print("            Working with the String Data Type              ")
print(".........................................................................................")

print("Exercise 1: Introducing the string data type")

myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
print(".........................................................................................")

print("Exercise 2: Working with string concatenation")

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
print(".........................................................................................")

print("Exercise 3: Working with input strings")
name = input("What is your name? ")
print(name)
print(".........................................................................................")

print("Exercise 4: Formatting output strings")

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))
print(".........................................................................................")
