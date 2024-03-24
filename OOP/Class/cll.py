# class car:
#     color = "blue"
#     brand = "BMW"
# car1 = car()
# print(car1.color)
# print(car1.brand)
class student:
    def __init__(self,fullname,marks):   # new object call self that is reference
        self.name = fullname
        self.marks = marks
        print("adding new student in database..")    
s1 = student("faiz",60)
print(s1.name,s1.marks)
