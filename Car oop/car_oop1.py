# Class is like a blueprint of the 

# attribute
# what an object is/has

# method
# what does it do

class Car:

# class variable
    wheels=4

# special method that create an object or constructor method
    def __init__(self,make,model,year,color):
        self.make=make      #instance variable
        self.model=model    #instance variable
        self.year=year      #instance variable
        self.color=color    #instance variable


# method of the class
    def drive(self):
        return "This "+self.model+" is driving"
    def stop(self):
        return "This "+self.model+" is stopping"
