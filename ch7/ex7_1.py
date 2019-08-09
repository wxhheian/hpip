# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
#
# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

# prompt = "If you tell us who you are,we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
#
# name = input(prompt)
# print("\nHello, " + name + "!")

# age = input("How old are you? ")
# print(int(age)>= 18)

number = input("Enter a number, and I'll tell you if it's even or odd:")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even")
else:
    print("\nThe number " + str(number) + " is odd.")
