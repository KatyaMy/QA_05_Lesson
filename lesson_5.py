# OOP and GIT/GIT HUB
# ''''вместо self можно поставить любой другой парметр, но это согласованное правило'''


class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def walk(self):
        return "I can walk!"


class Developer(Employee):
    def __int__(self, name, surname, language):
        super().__init__(name, surname)
        self.language = language

    def coding(self):
        return "I can coding!"


class Tester(Employee):
    def __int__(self, name, surname, language, test_frm):
        super().__init__(name, surname)
        self.language = language
        self.test_frm = test_frm


dev1 = Developer('Max', 'Foxl')

print(dev1.name())
print(dev1.walk())
print(dev1.coding())

tester1 = Tester('Anna', 'Ax', 'Java,', 'GT')

# employee1 = Employee('Alex', 'Smith')
# print(employee1.name)
# print(employee1.surname)
# print(employee1.walk())

# employee2 = Employee(surname='Popov', name='Vladimir')
# print(employee2.name)
# print(employee2.surname)
