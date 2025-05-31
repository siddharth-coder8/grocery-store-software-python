import datetime
import os

products = {
    "1": {"name": "Apple", "price": 4, "description": "Fresh and juicy apples."},
    "2": {"name": "Banana", "price": 3.5, "description": "Ripe and sweet bananas."},
    "3": {"name": "Orange", "price": 5, "description": "Tangy and juicy oranges."},
    # Add more products if needed
}

cart = []


def display_products():
    print("\nAvailable Products:")
    print("===================")
    for code, product in products.items():
        print(f"[{code}] {product['name']} - ₹{product['price']} - {product['description']}")
    print("===================")


def get_user_input():
    while True:
        product_code = input("Enter product code (or 'f' to finish): ").strip()
        if product_code.lower() == 'f':
            break
        elif product_code not in products:
            print("❌ Invalid code. Try again.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                raise ValueError
        except ValueError:
            print("❌ Invalid quantity. Must be a positive integer.")
            continue

        product = products[product_code]
        cart.append({
            "code": product_code,
            "name": product["name"],
            "price": product["price"],
            "description": product["description"],
            "quantity": quantity
        })


def calculate_total(cart):
    subtotal = sum(item["price"] * item["quantity"] for item in cart)
    tax = subtotal * 0.18  # 18% GST
    total = subtotal + tax
    return subtotal, tax, total


def generate_bill(cart, phone_number):
    now = datetime.datetime.now()
    filename = f"bill_{phone_number}_{now.strftime('%Y%m%d%H%M%S')}.txt"
    subtotal, tax, total = calculate_total(cart)

    with open(filename, "w") as f:
        f.write("🛒 ABC Grocery Store\n")
        f.write("="*30 + "\n")
        f.write(f"Phone: {phone_number}\n")
        f.write("Date: " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        f.write("-"*30 + "\n")
        for item in cart:
            line = f"{item['name']} x {item['quantity']} = ₹{item['price'] * item['quantity']:.2f}\n"
            f.write(line)
        f.write("-"*30 + "\n")
        f.write(f"Subtotal: ₹{subtotal:.2f}\n")
        f.write(f"Tax (18%): ₹{tax:.2f}\n")
        f.write(f"Total: ₹{total:.2f}\n")
        f.write("="*30 + "\n")
        f.write("🙏 Thank you for shopping with us!\n")

    print("\n✅ Bill generated and saved as", filename)
    return filename


def print_bill(filename):
    printer_name = "Canon_LBP2900"
    os.system(f'lp -d {printer_name} {filename}')
    print("🖨️ Bill sent to printer:", printer_name)


def main():
    print("💼 Welcome to ABC Grocery Store")
    display_products()
    get_user_input()

    if not cart:
        print("🛑 Cart is empty. Exiting.")
        return

    phone_number = input("Enter your phone number: ").strip()
    filename = generate_bill(cart, phone_number)

    print_option = input("Print the bill? (y/n): ").strip().lower()
    if print_option == 'y':
        print_bill(filename)


if __name__ == "__main__":
    main()
