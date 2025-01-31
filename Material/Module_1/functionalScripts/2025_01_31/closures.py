# Closures

def outerFunction ():
    message = 'Hello World'
    def innerFunction ():
        print (message)
    return innerFunction

if __name__ == '__main__':
    firstFunction = outerFunction ()
    firstFunction ()