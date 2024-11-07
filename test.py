# 📚 test_ebook_store.py

from ebook_store import EBook, Customer, ShoppingCart, PricingEngine, Invoice, Order

# 📖 Initialize the e-book catalog with 10 books
catalog = [
    EBook("Python Programming", "John Doe", "2021-01-15", "Programming", 15.99),
    EBook("Data Science Basics", "Jane Smith", "2020-07-22", "Data Science", 12.99),
    EBook("Machine Learning", "Alice Brown", "2019-11-10", "AI", 20.00),
    EBook("Deep Learning", "Bob White", "2018-09-25", "AI", 25.50),
    EBook("Introduction to Algorithms", "Charles Green", "2021-05-01", "Programming", 30.00),
    EBook("Ethical Hacking", "Diane Black", "2020-02-28", "Security", 18.75),
    EBook("Cybersecurity 101", "Elena Grey", "2019-12-15", "Security", 17.50),
    EBook("Blockchain Basics", "Frank Red", "2018-08-05", "Blockchain", 19.99),
    EBook("Networking Fundamentals", "Grace Blue", "2021-03-13", "Networking", 22.50),
    EBook("Cloud Computing", "Henry Purple", "2020-11-18", "Cloud", 27.00)
]

# ✏️ Modify an existing book in the catalog
catalog[0].price = 14.99  # 🏷️ Discount on "Python Programming"

# 👥 Initialize customers
customer1 = Customer("Aisha Almansoori", "aisha@example.com", "0504536436", is_loyalty_member=True)
customer2 = Customer("Mariam AlZaabi", "mariam@example.com", "0505743644", is_loyalty_member=True)
customer3 = Customer("Mansoor AlEmadi", "mansoor@example.com", "0521234567", is_loyalty_member=False)
customer4 = Customer("Latifa AlDhaheri", "latifa@example.com", "0549876543", is_loyalty_member=False)

# 🛠️ Initialize the pricing engine
pricing_engine = PricingEngine()

# 🛒 Create shopping carts for each customer
shopping_cart1 = ShoppingCart()
shopping_cart2 = ShoppingCart()
shopping_cart3 = ShoppingCart()
shopping_cart4 = ShoppingCart()

# 🎯 Testing Add, Delete, and Modify functionality in cart for Customer 1
# ➕ Add books to Aisha's cart
shopping_cart1.add_item(catalog[0])  # "Python Programming"
shopping_cart1.add_item(catalog[1])  # "Data Science Basics"
shopping_cart1.add_item(catalog[3])  # "Deep Learning"
print("🛍️ Aisha's Cart after adding items:")
for item in shopping_cart1.items:
    print(f"📘 - {item}")

# ➖ Remove a book and then ➕ add it again
shopping_cart1.remove_item(catalog[1])  # Remove "Data Science Basics"
print("\n🛍️ Aisha's Cart after removing 'Data Science Basics':")
for item in shopping_cart1.items:
    print(f"📘 - {item}")

shopping_cart1.add_item(catalog[1])  # Add "Data Science Basics" back
print("\n🛍️ Aisha's Cart after re-adding 'Data Science Basics':")
for item in shopping_cart1.items:
    print(f"📘 - {item}")

# 🎯 Testing Add, Delete, and Modify functionality in cart for Customer 2
# ➕ Add books to Mariam's cart with enough quantity to trigger the bulk discount
shopping_cart2.add_item(catalog[4])  # "Introduction to Algorithms"
shopping_cart2.add_item(catalog[5])  # "Ethical Hacking"
shopping_cart2.add_item(catalog[6])  # "Cybersecurity 101"
shopping_cart2.add_item(catalog[7])  # "Blockchain Basics"
shopping_cart2.add_item(catalog[8])  # "Networking Fundamentals"

print("\n🛍️ Mariam's Cart after adding items (bulk discount):")
for item in shopping_cart2.items:
    print(f"📘 - {item}")

# ➕ Adding items to Mansoor's cart (No discounts)
shopping_cart3.add_item(catalog[0])  # "Python Programming"
shopping_cart3.add_item(catalog[9])  # "Cloud Computing"

print("\n🛍️ Mansoor's Cart after adding items (No discounts):")
for item in shopping_cart3.items:
    print(f"📘 - {item}")

# ➕ Adding items to Latifa's cart (No discounts)
shopping_cart4.add_item(catalog[2])  # "Machine Learning"
shopping_cart4.add_item(catalog[4])  # "Introduction to Algorithms"

print("\n🛍️ Latifa's Cart after adding items (No discounts):")
for item in shopping_cart4.items:
    print(f"📘 - {item}")

# 📄 Generate and print invoices for each customer, testing discounts
invoice1 = Invoice(customer1, shopping_cart1, pricing_engine)
invoice2 = Invoice(customer2, shopping_cart2, pricing_engine)
invoice3 = Invoice(customer3, shopping_cart3, pricing_engine)
invoice4 = Invoice(customer4, shopping_cart4, pricing_engine)

# ➕ Create Orders for each customer
order1 = Order(order_id=1, order_date=invoice1.order_date, order_items=shopping_cart1.items, order_status="Completed")
order2 = Order(order_id=2, order_date=invoice2.order_date, order_items=shopping_cart2.items, order_status="Completed")
order3 = Order(order_id=3, order_date=invoice3.order_date, order_items=shopping_cart3.items, order_status="Completed")
order4 = Order(order_id=4, order_date=invoice4.order_date, order_items=shopping_cart4.items, order_status="Completed")

print("\n🧾 --- Customer 1 Invoice (Loyalty Discount) ---")
invoice1.generate_invoice()  # Invoice for Aisha with loyalty discount

print("\n🧾 --- Customer 2 Invoice (Bulk and Loyalty Discounts) ---")
invoice2.generate_invoice()  # Invoice for Mariam with bulk and loyalty discounts

print("\n🧾 --- Customer 3 Invoice (No Discounts) ---")
invoice3.generate_invoice()  # Invoice for Mansoor with no discounts

print("\n🧾 --- Customer 4 Invoice (No Discounts) ---")
invoice4.generate_invoice()  # Invoice for Latifa with no discounts

# ➕ Print order details for each customer
print("\n📦 --- Order Details ---")
for order in [order1, order2, order3, order4]:
    print(order)  # Display each order's details