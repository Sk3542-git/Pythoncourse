def addition(a,b): 
    return a+b
def subtraction(a,b):
    return a - b
def multiplaction(a,b):
    return a*b
def division(a,b):
    return a/b
print('please select opperations')
print('a. addition')
print('b. subtartion')
print('c. multiplycation')
print('d. division')
choice=input('Please enter you answer: ')
number1=int(input('Enter the value: '))
number2=int(input('Enter the value: '))
if choice == 'a':
    print(number1,' +',number2,'= ', addition(number1,number2 ))
elif choice == 'b':
    print(number1,' -',number2,'= ', subtraction(number1,number2 ))
elif choice == 'c':
    print(number1,'*',number2,'= ', multiplaction(number1,number2 ))
elif choice == 'd':
    print(number1,'/',number2,'= ', division(number1,number2 ))
else:
    print('Invaild oppsition')
     
