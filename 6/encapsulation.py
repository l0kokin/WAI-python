class Test:
    # გამოიყენება დოკუმენტაციისთვის
    _test: None #protected
    __test: None #private


class Invoice:
    def __init__(self, cost, from_person, to_person, credit_card):
        self._cost = cost
        self.from_person = from_person
        self.to_person = to_person
        self.__credit_card = credit_card

    def _set_cost(self, cost):
        name = input('Who are you?')
        if not name == self.from_person or name == self.to_person:
            print("you do not have the permission")
        self._cost = cost

    # def get_credit_card(self):
    #     getter_card = self.__credit_card // 10000
    #     return f"{getter_card}****"
    # or:
    @property
    def credit_card(self):
        getter_card = self.__credit_card // 10000
        return f"{getter_card}****"


    def __str__(self):
        return f"{self._cost}, {self.from_person}, {self.to_person}"


invoice = Invoice(5,'Person A', 'Person B', 23456789)
# invoice.cost = 10 #არ შეიცვლება
# # invoice._cost = 7 #შეიცვლება, მაგრამ ამის გაკეთება არ შეიძლება
# invoice.__cost = 10 #არ შეიცვლება
# print(invoice)

# invoice._set_cost(5)
# print(invoice.get_credit_card())
# or, if you're using @property:
print(invoice.credit_card)
