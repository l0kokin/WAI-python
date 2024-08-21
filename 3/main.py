list1 = []
for n in range(10):
    list1.append(n**2)

# exactly the same as:
list2 = [n+2 for n in range(10)]

print(list1)
print(list2)