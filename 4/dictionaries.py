# 1: copy - მუშაობს იგივენაირად რაც ლისტში
dict1 = {'key1': 'value1', 'key2': 'value2'}
dict2 = dict1.copy()

# 2: from keys
x = ['key1', 'key2', 'key3']
thisdict = dict.fromkeys(x, 0)
print(thisdict)

# 3: get
dict1 = {'key1': 'value1', 'key2': 'value2'}
print(dict1.get('key5', 'Nice try'))

# 4: items
dict1 = {'key1': 'value1', 'key2': 'value2'}
print(dict1.items())
for item in dict1.items():
    print(item, type(item))
# or unpack the items
for key, value in dict1.items():
    print(key, value)

# 5: keys
dict1 = {'key1': 'value1', 'key2': 'value2'}
keys = dict1.keys()
print(keys, type(keys))

# 6: pop - მუშაობს როგორც ლისტში ოღონდ ინდექსის მაგივრად უთითებ ქის
dict1 = {'key1': 'value1', 'key2': 'value2'}
dict1.pop('key2')
print(dict1)

# 7: popitem - ამოაგდებს ბოლო აითემს
dict1 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
dict1.popitem()
print(dict1)

# 8: setdefault
dict1 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
x = dict1.setdefault('key1', 'sali')
print(x)
x1 = dict1.setdefault('key5', 'sali')
print(x1)
print(dict1)
