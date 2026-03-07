class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def speak(self):
        f"Wooooowwwww {self.name}"
    def move(self):
        return f"Let go {self.name}"
evariste = Person("evariste",30)

print(evariste.move())
print(evariste.speak())
