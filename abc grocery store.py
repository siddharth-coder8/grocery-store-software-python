# grocery-store-software-python
# Define products and prices
import datetime

import os
from tabnanny import filename_only


products = {
    "1": {"name": "Apple", "price":4 , "description": "Fresh and juicy apples."},
    "2": {"name": "Banana", "price": 3.5, "description": "Ripe and sweet bananas."},
    "3": {"name": "Orange", "price": 5, "description": "Tangy and juicy oranges."},
    # Add more products here as needed
}

# Define a function to calculate the total price of all items in the cart
def calculate_total(cart):
    total = 0
    for item in cart:
        total += item["price"] * item["quantity"]
    return total

# Define an empty cart to store items
cart = []

# Ask the owner to input the products and quantities
while True:
    product_code = input("Enter the product code (or 'f' to finish): ")
    if product_code == "f":
        break
    elif product_code not in products:
        print("Invalid product code. Please try again.")
        continue
    quantity = int(input("Enter the quantity: "))
    cart.append({"code": product_code, "name": products[product_code]["name"], "price": products[product_code]["price"], "description": products[product_code]["description"], "quantity": quantity})

# Ask the customer for their phone number
phone_number = input("Enter your phone number: ")

# Calculate the total price
subtotal  = calculate_total(cart)
add = subtotal*18/100
total = add + subtotal
# Generate the bill
print("ABC Grocery Store")
print("=================")
print("Phone Number:", phone_number)
print("Date:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("-----------------")
for item in cart:
    print(item["price"] * item["quantity"])
print("-----------------")

print("-----------------")
print("Total: ", total,"Rs")
print("=================")
print("Thank you for shopping with us!")

# Save the bill to a file
filename = "bill_" + phone_number + ".txt"
with open(filename, "w") as f:
    f.write("ABC Grocery Store\n")
    f.write("=================\n")
    f.write("Phone Number: " + phone_number + "\n")
    f.write("Date: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    f.write("-----------------\n")
    for item in cart:
        f.write(item["name"] + " x " + str(item["quantity"]) + " = " + str(item["price"] * item["quantity"]) + "\n")
    f.write("-----------------\n")
    f.write("SubTotal: " + str(subtotal) + "\n")
    f.write("Tax: " + str(add) + "\n")
    f.write("Total: " + str(total) + "\n")
    f.write("=================\n")
    f.write("Thank you for shopping with us!\n")
print("Bill saved to", filename)


# Print the bill using a physical printer
printer_name = "Canon LBP2900"
os.system('lp -d ' + printer_name + ' ' + filename)
print("Bill printed on", printer_name)



