#QUES4
class Student:
    def __init__(self,student,roll_no):
        self.name=student
        self.roll_no=roll_no
    def __del__(self):
        print("object destroyed")

#creating object
student1=Student("harsh",21103096)
print("object created")
#printing the assigned values
print(f"the name of the student is {student1.name} and SID is {student1.roll_no}.")
#deleting object
del student1
