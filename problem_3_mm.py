"""
(Previous)Problem 2: Write a program that asks the user for her name and greets her with her name.
(Current) Problem 3: Modify the previous program such that only the users Alice and Bob are greeted with their names.
"""

if __name__ == "__main__":

    user_name = input("Please type your name: ")

    if user_name == "Alice" or user_name == "Bob":
        print("Hello " + user_name + "!")

    else:
        print("Welcome to the program")
