class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f'Hi, my name is {self.name}, and I am {self.age} years old.')

# test
p = person("Alice", 25)
p.introduce()
