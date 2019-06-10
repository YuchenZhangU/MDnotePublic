class Person:
  def __init__(self, names, ages):
    self.names = names
    self.ages = ages

p1 = Person(["John", "Ranran"], [36, 18])

n = p1.names
p1.names = None
print(n)
print(p1.names)

ls_a = [1,2,3]
ls_b = ls_a
ls_b = 0
print(ls_a)
print(ls_b)