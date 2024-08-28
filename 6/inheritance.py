class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'First name: {self.first_name}\nLast name: {self.last_name}'

class Parent:
    children = []
    def child_count(self):
        return len(self.children)

    def add_child(self, name):
        self.children.append(name)

    def __str__(self):
        return f"test"


class Doctor(Person, Parent):
    def __init__(self, first_name, last_name, hospital):
        super().__init__(first_name, last_name)
        self.hospital = hospital

    def __str__(self):
        return f'{super().__str__()}\nHospital: {self.hospital}'



doctor = Doctor('Sali', 'Gogishvili', 'N1')
print(doctor)
doctor.add_child('Ana')
print(doctor.child_count())