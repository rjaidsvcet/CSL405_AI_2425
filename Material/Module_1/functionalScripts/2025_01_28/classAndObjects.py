class GenericClass:
    def genericMethod (self, firstname, lastname):
        self.fname = firstname
        self.lname = lastname
        print (f'This is a generic method from {self.fname} {self.lname}')

if __name__ == '__main__':
    genericObject = GenericClass ()
    genericObject.genericMethod ('Arthur', 'Morgan')