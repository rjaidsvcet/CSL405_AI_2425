# Functions

# def nameOfFunction ():
#     print ('Hello World')

# def secondFunction ():
#     pass

# if __name__ == '__main__':
#     # secondFunction ()
#     nameOfFunction ()
#     nameOfFunction ()
#     nameOfFunction ()
#     nameOfFunction ()

# firstNumber, lastNumber = 10, 10

# def addition ():
#     newNumber = firstNumber + lastNumber
#     return newNumber

# def newAddition ():
#     return (firstNumber + lastNumber)

def internalDeclaration ():
    firstNum, lastNum = 10, 10
    summation = firstNum + lastNum
    return summation

def externalDeclaration (firstNum=0, lastNum=0):
    summation = firstNum + lastNum
    return summation

if __name__ == '__main__':
    firstVariable = internalDeclaration ()
    print (firstVariable)

    # firstNumber, secondNumber = 10, 10
    secondVariable = externalDeclaration (10,)
    print (secondVariable)
    # randomVariable = addition ()
    # secondRandomVariable = addition ()
    # newCalculation = randomVariable + secondRandomVariable
    # print (newCalculation)
