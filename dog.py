class Dog:
    def __init__(self,color,breed,name):
      self.color=color
      self.name=name
      self.breed=breed
    def run(self):
        return f'{self.name} of {self.color} are very fast. they are mostly {self.breed}'
