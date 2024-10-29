#create a class called person that has three attributes: name, age and gender,
#then create a constructor method and object

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"The name of my Favourite person is {self.name} he is a {self.gender} and is {self.age} years old")

    # create instance of a class (object)
    # An Object is an instance of a class


myobj = Person("Alex", "30", "Male")
myobj.display()