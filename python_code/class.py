class student(object):
    def __init__(self,name,rollno):
        self.name=input('enter the name')
        self.rollno=input('enter the roll no')
class graduate(student):
    def __init__(self,name,rollno,graduate):
        student .__init__(self,name,rollno)
        self.graduate=input('enter the degree')

    def display_graduate(self):
        print('student name',self.name)
        print('roll no',self.rollno)
        print('graduation',self.graduate)

class post_graduate(student):
    def __init_(self,name,rollno,postgraduate):
        student .__init__(self,name,rollno)
        self.postgraduate=input('enter the post graduation')
    def display_postgraduate(self):
        print('student name',self.name)
        print('roll no', self.rollno)
        print('post graduation',self.postgraduate)

GRAD=graduate()
POSTGRAD=post_graduate()
GRAD.display_graduate()
POSTGRAD.display_postgraduate()

