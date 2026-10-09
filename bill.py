
def calculate_bill(products):
    bill = 0

    for product in products:
        total_price = product["price"] * product["quantity"]
        product["total"] = total_price
        bill = bill + total_price

    return bill


products = []

for i in range(5):
    print("\nEnter details of product", i + 1)

    name = input("Enter product name: ")
    price = float(input("Enter product price: Rs. "))
    quantity = int(input("Enter quantity: "))

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    products.append(product)


bill = calculate_bill(products)

discount = 0

if bill > 10000:
    discount = bill * 0.10

final_bill = bill - discount

expensive_product = products[0]

for product in products:
    if product["price"] > expensive_product["price"]:
        expensive_product = product


print("\n----- Shopping Bill -----")

for product in products:
    print("Product:", product["name"])
    print("Price: Rs.", product["price"])
    print("Quantity:", product["quantity"])
    print("Total Price: Rs.", product["total"])
    print()

print("Complete Bill: Rs.", bill)
print("Discount: Rs.", discount)
print("Final Bill: Rs.", final_bill)

print("\nMost Expensive Product:", expensive_product["name"])
print("Product Price: Rs.", expensive_product["price"])


with open("bill.txt", "w") as file:
    file.write("----- Shopping Bill -----\n")

    for product in products:
        file.write("Product: " + product["name"] + "\n")
        file.write("Price: Rs. " + str(product["price"]) + "\n")
        file.write("Quantity: " + str(product["quantity"]) + "\n")
        file.write("Total Price: Rs. " + str(product["total"]) + "\n\n")

    file.write("Complete Bill: Rs. " + str(bill) + "\n")
    file.write("Discount: Rs. " + str(discount) + "\n")
    file.write("Final Bill: Rs. " + str(final_bill) + "\n")
    file.write("Most Expensive Product: " + expensive_product["name"] + "\n")
    file.write("Product Price: Rs. " + str(expensive_product["price"]) + "\n")

print("\nBill saved in bill.txt")

