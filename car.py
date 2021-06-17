class Car:
    type='Toyota'
    def __init__(self,color,mileage,make,registration):
      self.color=color
      self.mileage=mileage
      self.make=make
      self.registration=registration
    def accerelate(self):
        return f'Hello I am {self.color} {self.type}. I am are very fast. I accerelate at 345m per second'
    def hoot(self):
        return f'vroooooommmmm,,,, Big {self.color} {self.type} hoot that way'    
