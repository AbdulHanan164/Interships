class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self, product, quantity=1):
        self.items.append({'product': product, 'quantity': quantity})
    def remove_item(self, product_id):
        for item in self.items:
            if item['product'].id == product_id:
                self.items.remove(item)
                return True
        return False
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['product'].price * item['quantity']
        return total
    def get_total_quantity(self):
        total_quantity = 0
        for item in self.items:
            total_quantity += item['quantity']
        return total_quantity
class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.cart = ShoppingCart()
    def add_to_cart(self, product, quantity=1):
        self.cart.add_item(product, quantity)
    def remove_from_cart(self, product_id):
        return self.cart.remove_item(product_id)
# Function to display product details
def display_product_details(products):
    print("Product Details:")
    for product in products:
        print(f"ID: {product.id}, Name: {product.name}, Price: ${product.price}")

# Function to display customer details
def display_customer_details(customer):
    print("Customer Details:")
    print(f"ID: {customer.id}, Name: {customer.name}")
# Function to display cart details
def display_cart_details(customer):
    total_cost = customer.cart.calculate_total()
    total_quantity = customer.cart.get_total_quantity()
    print(f"Total cost for {customer.name}: ${total_cost}")
    print(f"Total quantity in cart: {total_quantity}")
if __name__ == "__main__":
    # Create some products
    product1 = Product(1, "Laptop", float(input("Enter the price of Laptop: ")))
    product2 = Product(2, "Smartphone", float(input("Enter the price of Smartphone: ")))
    product3 = Product(3, "Headphones", float(input("Enter the price of Headphones: ")))
    products = [product1, product2, product3]
    # Create a customer
    customer_name = input("Enter your name: ")
    customer = Customer(1, customer_name)
    while True:
        print("\nMenu:")
        print("1. Add to cart")
        print("2. Remove from cart")
        print("3. Display customer details")
        print("4. Display product details")
        print("5. Display cart details")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_product_details(products)
            product_id = int(input("Enter the ID of the product to add to cart: "))
            quantity = int(input("Enter the quantity: "))
            customer.add_to_cart(products[product_id - 1], quantity)
        elif choice == "2":
            product_id = int(input("Enter the ID of the product to remove from cart: "))
            customer.remove_from_cart(product_id)
        elif choice == "3":
            display_customer_details(customer)
        elif choice == "4":
            display_product_details(products)
        elif choice == "5":
            display_cart_details(customer)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
