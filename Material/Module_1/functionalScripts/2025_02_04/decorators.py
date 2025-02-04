def decoratorFunction (originalFunction):
    def wrapperFunction (*args, **kwargs):
        print ('Wrapper function executed this before original function')
        return originalFunction (*args, **kwargs)
    return wrapperFunction

@decoratorFunction
def displayFunction ():
    print ('This is a display function')

@decoratorFunction
def displayInformation (name, age):
    print (f'Display information for {name} and {age}')

if __name__ == '__main__':
    displayFunction ()
    displayInformation ('Bruce Wayne', 40)
    # decoratedDisplay = decoratorFunction (displayFunction)
    # decoratedDisplay ()

