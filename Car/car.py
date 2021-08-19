class Car :
    steeringwheel=1             #classlevelattribute
    def __init__(self,name,wheels):
        self.name=name          #instancelevelattribute
        self.wheels=wheels      #instancelevelattribute

    def drive(self):
        print(f'{self.name} is driving.')

    @classmethod                #classlevelmethod or classlevelfunction
    def common(cls):
        print(f'everycar has only {cls.steeringwheel} steering wheel.')

# lambo=Car("lambo",4)
# print(lambo.name) 
# lambo.drive()

# mercedez=Car("Mercedez",4)
# print(mercedez.name)
# mercedez.drive()
Car.common()