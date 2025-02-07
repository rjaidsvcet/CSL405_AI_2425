from contextlib import contextmanager

@contextmanager
def genericFileFunction (filename, method):
    print ('Enter')
    file = open (filename, method)
    yield file
    print ('Exit')

if __name__ == '__main__':
    with genericFileFunction ('./file.txt', 'w') as f:
        print ('Middle')
        f.write ('Content from ContextLib')