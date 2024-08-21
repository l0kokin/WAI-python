# Lambda function - used like an arrow function in callbacks etc

# ეს ორი ერთი და იგივეა:
def lambda_function(x):
    print(f'our objext {x}')
lambda x:print(f'Our object {x}') 


numbers = [1,2,3,4,5,6]
# example N1:
even_numbers = filter(lambda x: x%2 == 0, numbers)
print(list(even_numbers))

# example N2:
# ** 2-ის ხარისხში აყვანაა
result = list(map(lambda x: x**2, numbers))
print(result)