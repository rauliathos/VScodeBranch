class Student:

    def __init__(self, name="student", age="student", class_="student"):
        self.name = name
        self.age = age
        self.class_ = class_

    def averageScore (self, a,b,c):
        average = (a+b+c)/3
       #
        return f"{self.name} average score is : {average}" 


