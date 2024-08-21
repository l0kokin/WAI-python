# 1: positional arguments
def say_hi(firstname, lastname):
    print(f'Hello {firstname} {lastname}')

say_hi('Sali', 'Gogishvili')


# 2: keyword arguments
def say_hi(firstname, lastname):
    print(f'Hello {firstname} {lastname}')

say_hi(lastname='Gogishvili', firstname='Sali')


# 3: default arguments
def say_hi(firstname, lastname=None):
    if lastname:
        print(f'Hello {firstname} {lastname}')
    else:
        print( f'Hello {firstname}')

say_hi('Sali')


# 4: arbitrary arguments
def say_hi(*names):
    for name in names:
        print(f'Hello {name}')

say_hi('Nika', 'Sali', 'Mariam', 'Ana')


# 5: arbitrary keyword arguments
def say_hi(**args):
    for firstname, lastname in args.items():
        print(f'hi {firstname} {lastname}')
# აქ დიქშენარიდ გადაიქცევა არგუმენტები ქი ველიუ წყვილებად
say_hi(nika='mdinaradze', mariam='dumbadze', sali='gogishvili')


#  6: positional only arguments
def say_hi(firstname, lastname, /, greeting='Hello'):
    print(f'{greeting} {firstname} {lastname}')

say_hi('Sali', 'Gogishvili')


# 7: keyword only arguments
def say_hi(*, firstname, lastname):
    print(f'Hello {firstname} {lastname}')

say_hi(firstname='Sali', lastname='Gogishvili')


# 8: touple unpacking
def say_hi(firstname, lastname):
    print(f'Hello {firstname} {lastname}')

fullname = ('Sali', 'Gogishvili')
# we're touple unpacking. also works with lists and sets (but this one is unordered)
say_hi(*fullname)


# 9: dictionary unpacking
def say_hi(firstname, lastname):
    print(f'Hello {firstname} {lastname}')

fullname = {'firstname':'Sali', 'lastname':'Gogishvili'}

say_hi(**fullname)


# 10: reccursion 
# თავის თავში გამოძახება ფუნქციის
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(4)
print(result)


# 11: higher-order function
def alert(func):
    print('function is running...')
    func()

def display():
    print('test')

alert(display)