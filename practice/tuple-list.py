from collections import namedtuple

Fruit = namedtuple("Fruit", ["name", "color", "other"])
f = Fruit(name = "banana", color = "red", other = "notset")
print(f)

print(f.name)
print(f.color)
f = Fruit(name = 1, color = "2", other = 100)
print(f)

print(f.name)
print(f.color)
