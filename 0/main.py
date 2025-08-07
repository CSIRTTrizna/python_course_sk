# Premenne

example_string: str = "Test String"
example_boolean: bool = True
example_integer: int = 64
example_float: float = 64.32
example_array: list = [1, 2, "element1", "element2"]

# Podmienky

if example_integer > 100:
    print(">100")
elif example_integer > 50:
    print(">50")
else:
    print("small")


# Cykly
for number in range(10):
    print(number)


number = 0

while number < 10:
    print(number)
    number += 1



number = 0

while True:
    print(number)
    number += 1
    if number >= 10:
        break


# Funkcie / metody

def divide(number1, number2):
    if number2 == 0:
        return 9e99
    return number1 / number2

print(divide(4, 2))
print(divide(4, 0))


# Triedy + magicke metody

class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def __repr__(self):
        return self.name
    
    def __gt__(self, other):
        return self.weight > other.weight


fero = Person("Ferko", 80)
jozo = Person ("Jozko", 90) 

print(fero > jozo)
print(fero < jozo)

print(fero, jozo)

classroom = [fero, jozo, fero, jozo]

print("Ascending: ")
print(sorted(classroom))

print("Descending: ")
print(sorted(classroom, reverse=True))
