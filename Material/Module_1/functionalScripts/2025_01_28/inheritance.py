class Student:
    attendance = 0.75
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.email = firstname.lower() + '.' + lastname.lower() + '@college.edu.in'

    def fullname (self):
        return '{} {}'.format (self.firstname, self.lastname)

class Senior (Student):
    def __init__ (self, name, lastname, placed : bool = False):
        super ().__init__ (name, lastname)
        self.employed = placed

# class Sophomore (Student):
#     pass

if __name__ == '__main__':
    firstStudent = Senior ('Raju', 'Rastogi', placed=True)
    secondStudent = Senior ('Rancho', 'Chhachad', placed=False)
    # print (firstStudent.__dict__)
    print (firstStudent.attendance)
    firstStudent.attendance = 0.65
    print (firstStudent.__dict__)
    print (secondStudent.attendance)

