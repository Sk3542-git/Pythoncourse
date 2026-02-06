numd=int(input('Enter an numerator: '))
dn=int(input('Enter an denominator: '))
if numd % dn == 0:
    print(numd,'Is divisible by',dn) 
else:
    print(numd,'Is not divisible by',dn)