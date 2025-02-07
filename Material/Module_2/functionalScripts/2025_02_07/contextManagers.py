class File:
    def __init__(self, filename, method):
        self.file = open (filename, method)

    def __enter__ (self):
        print ('Enter Method Executed')
        return self.file
    
    def __exit__ (self, type, value, traceback):
        print (f'{type}, {value}, {traceback}')
        print ('Exit Method Executed')
        self.file.close ()
        if type == Exception:
            return True

if __name__ == '__main__':
    with File ('./file.txt', 'w') as f:
        print ('Middle Method Executed')
        f.write ('Some generic content')
        raise Exception ()