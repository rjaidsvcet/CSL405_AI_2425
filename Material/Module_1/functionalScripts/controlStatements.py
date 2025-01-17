firstVariable = int (input ('Enter first number\n'))
secondVariable = int (input ('Enter second number\n'))
thirdVariable = int (input ('Enter third number\n'))
fourthVariable = int (input ('Enter fourth number\n'))

if (firstVariable == secondVariable) and \
    (thirdVariable == fourthVariable):
    print ('Done')
elif (firstVariable == secondVariable) or \
    (thirdVariable == fourthVariable):
    print ('OR Operation used')

# if (firstVariable == secondVariable):
#     print ('Equals')
# elif (firstVariable < secondVariable):
#     print ('Less Than')
# elif (firstVariable > secondVariable):
#     print ('Greater Than')
# else:
#     print ('Nothing')

