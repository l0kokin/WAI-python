inventory_db = {
    1: {"item_name": "Laptop", "quantity": 10, "price": 999.99, "tags": {"electronics", "computers"}},
    2: {"item_name": "Mouse", "quantity": 50, "price": 19.99, "tags": {"electronics", "accessories"}},
    3: {"item_name": "Keyboard", "quantity": 30, "price": 49.99, "tags": {"electronics", "accessories"}},
    4: {"item_name": "Monitor", "quantity": 15, "price": 149.99, "tags": {"electronics", "displays"}},
    5: {"item_name": "Printer", "quantity": 5, "price": 89.99, "tags": {"electronics", "office"}},
}

def get_item(item_id: int):
    item = inventory_db.get(item_id)
    if not item:
        print('Item not found')
        return
    print('Details')
    print('== ' * 10)
    print(f'ID: {item_id}')
    print(f'Name: {item['item_name']}')
    print(f'Quantity: {item['quantity']}')
    print(f'Price: ${item['price']}')
    tags = ', '.join(item['tags'])
    print(f'Tags: {tags}')
    print('== ' * 10)

def update_quantity(item_id, quantity):
    item = inventory_db.get(item_id)
    if not item:
        print('Item not found')
        return
    if quantity < 0:
        return "Quantity cannot be negative"
    if quantity == 0:
        inventory_db.pop(item_id)
        return 'Item has been removed'
    item['quantity'] = quantity
    return item

item = update_quantity(1,20)
print(item)
item = get_item(1)
