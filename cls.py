class Person:
  def __init__(self ,name, age):
    self.name = name
    self.age = age
    print(f"my name is : {name}i am {age} year old")

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("Antim", 19)
p1.myfunc()


print("----------------------------------")

class Student:
    # class variables
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

s1 = Student("Harry", 12)
# access instance variables
print('Student:', s1.name, s1.age)

# access class variable
print('School name:', Student.school_name)

# Modify instance variables
s1.name = 'Jessa'
s1.age = 14
print('Student:', s1.name, s1.age)

# Modify class variables
Student.school_name = 'XYZ School'
print('School name:', Student.school_name)