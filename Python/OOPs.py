class Employee:
    empCount = 0;
    
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
        Employee.empCount += 1;
        
    def printEmployee(self):
        print(self.name + ": " + str(self.age));
        
    def printCount(self):
        print(Employee.empCount);
        
emp1 = Employee("nandita", 23);
emp2 = Employee("sabhya", 23);

#emp1.printEmployee();
#emp2.printEmployee();
#print(Employee.empCount)

"""
print(emp1.name)
print(emp2.age)

print(getattr(emp1, "age"))
"""
emp1.printEmployee();
setattr(emp1, "beauty", "unparalleled");
emp1.printEmployee();