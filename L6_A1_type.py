# Python program to illustrate the use

# of 'is' identity operator


x = 5

if (type(x) is int):

    print("true")

else:

    print("false")

 
x = 5.5

if (type(x) is not float):

    print("true")

else:

    print("false")

 
x = 20

y = 40

if (x is y):

    print("x & y SAME identity")
else:
    print('X and Y arent the same identity')

 
y = 20

if (x is not y):

    print("x & y have DIFFERENT identity")
else:
    print('x and Y are the same identity')