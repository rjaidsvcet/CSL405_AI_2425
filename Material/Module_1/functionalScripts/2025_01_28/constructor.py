class Student:
    def __init__ (self, firstname, lastname):
        self.fname = firstname
        self.lname = lastname
        self.email = firstname.lower() + '.' + lastname.lower() + '@college.edu.in'

    def fullname (self):
        return f'The name of student is {self.fname} {self.lname} and email is {self.email}'

if __name__ == '__main__':
    firstStudent = Student ('Trevor', 'Philips')
    print (firstStudent.fullname ())
    secondStudent = Student ('Niko', 'Bellic')
    print (secondStudent.fullname ())