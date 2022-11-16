# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def say_hi(self):
#         print(f"Hello, my name is {self.name}. How are you?")
#
# p = Person('Kalya')
# p.say_hi()
# Person('Jack').say_hi()


# class Robot:
#     """Represents a robot with a name"""
#
#     population = 0
#
#     def __init__(self, name):
#         """Initializes the data"""
#         self.name = name
#         print("Initializing : {}".format(self.name))
#
#         # When the robot is created, add to population count
#         Robot.population += 1
#
#     def die(self):
#         """I am dying"""
#         print(f"{self.name} is being destroyed!")
#
#         Robot.population -= 1
#
#         if Robot.population == 0:
#             print("{} was the last one.".format(self.name))
#         else:
#             print("There are still {:d} robots working.".format(Robot.population))
#
#     def say_hi(self):
#         """Greeting by the robot.
#
#         Yes, they can do that. :D"""
#         print(f"Greetings. My masterse call me {self.name}")
#
#     @classmethod
#     def how_many(cls):
#         """Prints the current robot population"""
#         print("We have {:d} robots.".format(cls.population))
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# Robot.how_many()
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# Robot.how_many()
#
# print("\nRobots can do some work here.\n")
#
# print("Robots have finished their work. So let's destroy them.")
# droid1.die()
# droid2.die()
#
# Robot.how_many()
# print(Robot.__doc__)
# print(Robot.say_hi.__doc__)


class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f'(Initialized SchoolMember: {self.name})')

    def tell(self):
        '''Tell my details.'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mdm Tan', 54, 36000)
s = Student('Kalya', 30, 87)

# prints a blank line
print()

members = [t, s]

for member in members:
    member.tell()