Shiks_caffe = {
    '1': {'name': 'Chips', 'price': 10.0},
    '2': {'name': 'Candy', 'price': 5.0},
    '3': {'name': 'Soda', 'price': 15.0},
    '4': {'name': 'Water', 'price': 12.0},
    '5': {'name': 'milk', 'price': 20.0},
    '6': {'name': 'popcorn', 'price': 5.0},
    '7': {'name': 'candy', 'price': 15.0},
    '8': {'name': 'sand', 'price': 45.0},
    '9': {'name': 'Gely', 'price': 25.0},
    '10': {'name': 'banana_chips', 'price': 25.0}
}
print("\t\t\t\t!!!!    Welcome to the VenderMachine  !!!!!!!\t\t\t")
qtn = input("Do you want to see the menu? (yes/no): ")
#
if qtn.lower() == 'yes':
    print("-----------------------------------------------------------------")
    print("prod_id\t\t\tname\t\t\tPrice")
    print("-----------------------------------------------------------------")
    for key, val in Shiks_caffe.items():
        name = val['name']
        price = val['price']
        menu = print(f"{key}\t\t\t\t{name}\t\t\t{price}")
        print("-----------------------------------------------------------------")
        print("-----------------------------------------------------------------")

cart = {}
total_amount = 0

while True:
    prod_id = input("Enter the product ID you want to purchase (or 'q' to quit): ")

    if prod_id.lower() == 'q':
        break

    if prod_id not in Shiks_caffe:
        print("Invalid product ID. Please try again.")
        continue

    quantity = int(input("Enter the quantity: "))

    if quantity <= 0:
        print("Invalid quantity. Please try again.")
        continue

    item = Shiks_caffe[prod_id]
    name = item['name']
    price = item['price']

    if prod_id in cart:
        cart[prod_id]['quantity'] += quantity
    else:
        cart[prod_id] = {
            'name': name,
            'price': price,
            'quantity': quantity
        }

    total_amount += price * quantity

    print(f"{name} (Quantity: {quantity}) ")
    print("U want added Another Product to cart.")
    print("-----------------------------------------------------------------")

print("\n--- Your Cart ---")
if len(cart) == 0:
    print("Your cart is empty.")
else:
    print("prod_id\t\tname\t\t\t\tprice\t\tquantity\t\tamount")
    print("-----------------------------------------------------------------")
    for key, val in cart.items():
        prod_id = key
        name = val['name']
        price = val['price']
        quantity = val['quantity']
        amount = price * quantity
        print(f"{prod_id}\t\t\t{name}\t\t\t\t{price}\t\t{quantity}\t\t\t{amount}")
    print("-----------------------------------------------------------------")
    print(f"Total amount: {total_amount}")

def calculate_change(total_amount, paid_amount):
    change = paid_amount - total_amount
    return change

paid_amount = 0
coins_10 = 0
coins_5 = 0

while paid_amount < total_amount:
    coin = int(input("Enter the coin value (10 or 5): "))

    if coin == 10:
        coins_10 += 1
        paid_amount += 10
    elif coin == 5:
        coins_5 += 1
        paid_amount += 5
    else:
        print("Invalid coin value. Please try again.")

if paid_amount < total_amount:
    print("Insufficient amount. Payment failed.")
else:
    change = calculate_change(total_amount, paid_amount)
    print(f"Change: {change}")
    print("Payment successful. Thank you for shopping at VenderMachine!")

    if coins_10 > 0:
        print(f"Number of 10 rupee coins: {coins_10}")
    if coins_5 > 0:
        print(f"Number of 5 rupee coins: {coins_5}")