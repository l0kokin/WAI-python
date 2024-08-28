class Database:
    store = {
        1: ['Sali', 'Gogishvili', 27],
        2: ['Ana', 'Mdinaradze', 20],
        3: ['Sopo', 'Opla', 30]
    }
    # pk = primary key
    last_pk = 1

    def add_person(self, first_name, last_name, age):
        self.store[self.last_pk] = [first_name, last_name, age]
        self.last_pk += 1

    def _check_person(self, pk):
        person = self.store.get(pk)
        if not person:
            print('Not found')
        return person

    def get_person(self, pk):
        person = self._check_person(pk)
        if not person:
            return
        print('-' * 10)
        print(f"First name: {person[0]}\nLast name: {person[1]}\nAge: {person[2]}")
        print('-' * 10)

    def all_persons(self):
        for pk, person in self.store.items():
            print('-' * 10)
            print(f"PK: {pk}\nFirst name: {person[0]}")
            print('-' * 10)

    def delete_person(self, pk):
        person = self._check_person(pk)
        if not person:
            return
        self.store.pop(pk)


database = Database()
database.add_person('Kita', 'Askilashvili', 28)
database.add_person('Irakli', 'Bubu', 32)
database.add_person('Lalo', 'Opi', 82)
database.get_person(1)
database.all_persons()
database.delete_person(200)