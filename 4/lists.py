# ლისთების მეთოდები:

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1: append ამატებს ელემენტს ბოლოში
list1.append(10)
print(list1)

# 2: clear აცარიელებს მთლიანად
list1.clear()
print(list1)

# 3: copy აკეთებს ასლს
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, list1.copy()]
list2[-1].append(5)
print(list2[-1])
print(list1)

# 4: count დაითვლის ელემენტი რამდენჯერ გვხვდება
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 5]
print(list1.count(5))

# 5: extend გადააბამს
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = (1, 2, 3, 4, 5, 6)
list1.extend(list2)
print(list1)

# 6: index ელემენტი მერამდენეა ლისტში გეუბნება
list1 = [2, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1.index(2))

# 7: index
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list1.insert(2, 10)
print(list1)

# 8: pop(index) and remove(el) შლის
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list1.pop(1)
list1.remove(9)
print(list1)

# 9: sort
list1 = [2, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list1.sort()
list2 = ['a', 'd', 'f', 'c', 'h']
list2.sort()
print(list2)