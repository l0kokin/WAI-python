# 1: if else statements
total_amount = float(input('total amount: $'))

if total_amount <= 0:
    print("Invalid price")
else:
    if total_amount > 100:
        total_amount *= 0.9

    elif 50<= total_amount<=100:
        total_amount *= 0.95

    elif total_amount < 50:
        # total_amount
        pass

    print(f"Discounted price is {total_amount}")


# 2: same logic with while loop
while True:
    user_input = input('total amount in dollars (press Q to quit): ')
    if user_input == 'Q':
        break
    
    total_amount = float(user_input)
    if total_amount <= 0:
        print("Invalid price")
    else:
        if total_amount > 100:
            total_amount *= 0.9

        elif 50<= total_amount<=100:
            total_amount *= 0.95

        elif total_amount < 50:
            pass

        print(f"Discounted price is {total_amount}")


# 3: calculate discounted prices for items
items = [
    {
        "name": "laptop",
        "price": 800
    },
    {
        "name": "ball",
        "price": 10
    }, 
    {
        "name": "car",
        "price": 2600
    }
]

n = 0
while n != len(items):
    price = items[n]['price']

    if price <= 0:
        print("Invalid price")
    else:
        if price > 100:
            price *= 0.9

        elif 50<= price<=100:
            price *= 0.95

    print(f"Discounted price for {items[n]['name']} is {price}")
    n += 1


# 4: same with a for loop
for item in items:
    if item['price'] <= 0:
        print("Invalid price")
    else:
        if item['price'] > 100:
            item['price'] *= 0.9

        elif 50<= item['price']<=100:
            item['price'] *= 0.95
        
    print(f"Discounted price for {item['name']} is {item['price']}")


# 5: more examples
while True:
    user_input = input('total amount in dollars (press Q to quit): ')
    if user_input == 'Q':
        break
    elif not user_input.isnumeric():
        continue
    
    total_amount = float(user_input)
    if total_amount <= 0:
        print("Invalid price")
    else:
        if total_amount > 100:
            total_amount *= 0.9

        elif 50<= total_amount<=100:
            total_amount *= 0.95

        print(f"Discounted price is {total_amount}")