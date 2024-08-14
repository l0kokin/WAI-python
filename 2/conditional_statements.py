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