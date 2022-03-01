#QUES5
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
#creating employee records
employee1 = Employee("mehak", 40000)
employee2 = Employee("ashok", 50000)
employee3 = Employee("viren", 60000)

#part(a)updating salary
employee1.salary = 70000
print(f"(a)the updated salary of {employee1.name} is {employee1.salary}")

#part(b)deleting a record
print("(b)record of viren deleted", end='')
del employee3
