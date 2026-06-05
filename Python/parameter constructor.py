class Student:
    def __init__ (self, name, marks):
        #marks = [98, 99, 95]
        self.name = name
        self.marks = marks
    def get_avg (self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi, your avg score is:", sum/3)
        
s1 = Student("Tony Stark", [99, 98, 97])
print(s1.name)
print("Marks of 3 subjects =", s1.marks)
s1.get_avg()