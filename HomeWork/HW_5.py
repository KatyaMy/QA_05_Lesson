"""Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
    - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута 
    нужно использовать методы get и set"""""


class Cat:
    def __init__(self, name, age, weight,sex):
        self.name = name
        self.age = age
        self.weight = weight
        self.sex = sex

    def get_name(self):
        print(f'Cats name is: {self.name}')

    def get_age(self):
        print(f"Age: {self.age} y.o")

    def get_weight(self):
        print(f'Weigth: {self.weight} kg')

    def get_sex(self):
        print(f'Sex: {self.sex} ')


cat1 = Cat('Motz', 2, 9, 'M')
cat1.get_name()
cat1.get_age()
cat1.get_weight()
cat1.get_sex()
print('------------------')
cat2 = Cat('Bell', 1, 5, 'F')
cat2.get_name()
cat2.get_age()
cat2.get_weight()
cat2.get_sex()




