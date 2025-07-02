from abc import ABC, abstractmethode

class BluePrint(ABC):
  def __init__(self):
    self.name = "Jamal Nuklir"
    self.age = 19
    self.height = 175
  def __str__(self):
    return f"Let me introduce this self, name is {self.name} and is {self.age} years old"
  @abstractmethod
  def sound(self):
    return

class Cat(BluePrint):
  def __init__(self):
    super().__init__()
  def sound(self):
    return "Woof—woof—woof"

cat = Cat()
print(cat.sound())
