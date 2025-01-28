class Student:
    attendance = 0.75
    def __init__ (self, firstname, lastname):
        self.fname = firstname
        self.lname = lastname
        self.email = firstname.lower() + '.' + lastname.lower() + '@college.edu.in'

    def fullname (self):
        return f'The name of student is {self.fname} {self.lname} and email is {self.email}'
    
    def __repr__ (self):
        return '{} {}'.format (self.fname, self.lname)
    
    def __str__(self):
        return f'{self.email}'
    
    def __add__ (self):
        return (self.attendance + self.attendance)
    
if __name__ == '__main__':
    firstStudent = Student ('Lara', 'Croft')
    print (firstStudent.__add__())