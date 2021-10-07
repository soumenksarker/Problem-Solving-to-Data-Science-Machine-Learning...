class person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def tell(self):
        print('Hey , my name is {} and my age is {}'.format(self.name, self.age))
person(21,'prianka').tell()
