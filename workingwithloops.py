print("              Working with loops              ")
print(".........................................................................................")

print("Exercise 1: Working with a while loop")
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
print(".........................................................................................")
print("              Importing random and writing a while loop                ")
#Note: By convention, import statements are placed at the top of the script.
import random
#Place the cursor on the next line after the second print() statement. Next, enter a statement that will generate a random number between 1 and 10 by using the randint() function of the random module
number = random.randint(1,10)
#Track whether the user guessed your number by creating a variable called isGuessRight:
isGuessRight = False
#To handle the game logic, create a while loop:
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        #To inform the user about your script, use the print() function:
print("Count to 10!")
#Python uses indentation to determine that the print statement is inside the for loop statement.):
for x in range (0, 11):
    print(x)

      
      
