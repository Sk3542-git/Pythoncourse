# Get input from user

char = input("Enter a single character: ")


# Validate: Check if exactly one character

if type(char) is str and len(char) == 1:

    print("Valid input!")

else:

    print("Please enter exactly ONE character!")