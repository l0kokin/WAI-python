# 1: difference - განსხვავებულ ელემენტებს აბრუნებს
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

# 2: difference_update - იგივეს შვება ოღონდ თან შლის დუპლიკატს
x.difference_update(y)
print(x)

# 3: discard
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

# 4: intersection - საერთო ელემენტს აბრუნებს
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

# 5: intersection_update - საერთო ელემენტს აბრუნებს და თან შლის ყველა სხვას
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# 6: isdisjoint - საერთო ელემენტი თუ აქვთ ამოწმებს
x = {"apple", "banana", "cherry", "microsoft"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

# 7: issubset - ქვესიმრავლე თუა ამოწმებს
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

# 8: pop - შლის რენდომ ელემენტს
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

# 9: symmetric_difference - ორივე სეტიდან აბრუნებს ყველაფერს იმის გარდა რაც საერთო ქონდათ
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

# 10: symmetric_difference_update - რაც საერთო იყო წაშლის, რაც არ იყო საერთო ჩაამატებს
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference_update(y)
print(x)

# 11: union - ახალ სეტს შექმნის სადაც ამათი ყველა ელემენტია დუპლიკატების გარეშე
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

# 12: update - იგივე სეტს შეცვლის, ჩაუმატებს მეორეს ახალ ელემენტებს
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)