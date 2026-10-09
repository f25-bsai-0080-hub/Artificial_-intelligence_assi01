
def calculate_bill(orders):
    total_bill = 0

    for item in orders:
        total_bill = total_bill + item["total"]

    return total_bill


menu = {
    1: {"name": "Burger", "price": 500},
    2: {"name": "Pizza", "price": 800},
    3: {"name": "Fries", "price": 250},
    4: {"name": "Drink", "price": 150}
}

orders = []

while True:
    print("\n----- Restaurant Menu -----")
    print("1. Burger  - Rs. 500")
    print("2. Pizza   - Rs. 800")
    print("3. Fries   - Rs. 250")
    print("4. Drink   - Rs. 150")
    print("5. Finish Order")

    choice = int(input("Select an item: "))

    if choice == 5:
        break

    elif choice >= 1 and choice <= 4:
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            name = menu[choice]["name"]
            price = menu[choice]["price"]
            total = price * quantity

            order = {
                "name": name,
                "price": price,
                "quantity": quantity,
                "total": total
            }

            orders.append(order)

            print(name, "Total Price = Rs.", total)

        else:
            print("Invalid quantity!")

    else:
        print("Invalid choice!")


bill = calculate_bill(orders)

print("\n----- Final Bill -----")

for item in orders:
    print(item["name"], "-", item["quantity"],
          "x Rs.", item["price"],
          "= Rs.", item["total"])

print("Total Bill = Rs.", bill)

with open("orders.txt", "w") as file:
    file.write("----- Restaurant Bill -----\n")

    for item in orders:
        file.write(
            item["name"] + " - " +
            str(item["quantity"]) + " x Rs. " +
            str(item["price"]) + " = Rs. " +
            str(item["total"]) + "\n"
        )

    file.write("Total Bill = Rs. " + str(bill))

print("\nOrder saved in orders.txt")
