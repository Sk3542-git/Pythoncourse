Sale_amount=float(input('Enter the sale amount: '))
irlamount=float(input('Enter the irl amount: '))
if (irlamount > Sale_amount):
    amount=Sale_amount - irlamount
    print('Your profit is',amount)
else:
    amount=Sale_amount - irlamount
    print('No profit',amount)
