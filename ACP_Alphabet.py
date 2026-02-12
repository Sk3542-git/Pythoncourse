char = input("Enter a character: ")

if len(char) == 1:
    if char.isalpha():
        print("The entered character is an alphabet.")
    else:
        print("The entered character is NOT an alphabet.")
else:
    print("Please enter only a single character.")