# modify the previous program such that only the users Alice and Bob are greeted with their names.


if __name__ == "__main__":
    name = input("what's your name ?\n")
    if name == "Alice" or name == "Bob":
       print("Hello, " + name)
    else:
       print("Hello!")
