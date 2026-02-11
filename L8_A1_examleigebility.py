medic=input('Do you have a medical codition Y or N: ')
n=int(input('What is your attendance percentage: '))
if medic == 'Y': 
    print('Allow student for the exam. ')
else:
    if n >= 75:
        print('Allow student for the exam.')
    else:
        print('Student not allowed for exam.')