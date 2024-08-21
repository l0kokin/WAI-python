list1 = [n**2 for n in range(100) if n%2==0]
print(list1)

dict1 = {f'key{n}': f'value{n}' for n in range(10) if n%2==1}
print(dict1)

