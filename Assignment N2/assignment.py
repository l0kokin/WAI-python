def apply_operation(numbers, operation):
    return [operation(number) for number in numbers]


# doubling elements
result1 = apply_operation(operation=lambda n: n*2, numbers=[1,2,3,4,5])

# squaring elements
result2 = apply_operation(operation=lambda n: n**2, numbers=[1,2,3,4,5])

# filtering odd numbers
filtered_numbers = list(filter(lambda n: n%2 == 1, [1,2,3,4,5]))
result3 = apply_operation(operation=lambda n: n, numbers=filtered_numbers)


print(result1)
print(result2)
print(result3)