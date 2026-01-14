amount=int(input('Enter the amount to withdraw: '))

note1=amount//100
note2=(amount%100) //50
note3=((amount%100) %50) //10

print('We have 100 dollor bills in amount is: ',note1)
print('We have 50 dollor bills in amount is: ',note2)
print('We have 10 dollor bills in amount is: ',note3)