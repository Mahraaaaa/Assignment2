from datetime import datetime

class EBook:
    """Represents an e-book with various details."""

    def __init__(self, title, author, pub_date, genre, price):
        self._title = title
        self._author = author
        self._pub_date = pub_date
        self._genre = genre
        self._price = price

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def pub_date(self):
        return self._pub_date

    @property
    def genre(self):
        return self._genre

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self._price = new_price
        else:
            raise ValueError("Price cannot be negative")

    def __str__(self):
        return f"{self._title} by {self._author} ({self._pub_date}, {self._genre}) - ${self._price:.2f}"


class Customer:
    """Represents a customer with personal information and purchase history."""

    def __init__(self, name, email, phone, is_loyalty_member):
        self._name = name
        self._email = email
        self._phone = phone
        self._purchase_history = []
        self._is_loyalty_member = is_loyalty_member

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def phone(self):
        return self._phone

    @property
    def purchase_history(self):
        return self._purchase_history

    @property
    def is_loyalty_member(self):
        return self._is_loyalty_member

    @is_loyalty_member.setter
    def is_loyalty_member(self, loyalty_status):
        self._is_loyalty_member = loyalty_status

    def add_purchase(self, ebook):
        self._purchase_history.append(ebook)

    def view_purchases(self):
        for purchase in self._purchase_history:
            print(purchase)

    def __str__(self):
        return f"{self._name} ({self._email}, {self._phone})"


class Order:
    """Represents an order placed by a customer."""

    def __init__(self, order_id, order_date, order_items, order_status):
        self.order_id = order_id
        self.order_date = order_date
        self.order_items = order_items  # This should be a list of EBook objects
        self.order_status = order_status

    def __str__(self):
        # Create a string of e-book titles from the order items
        items_titles = ', '.join(item.title for item in self.order_items)
        return f"Order ID: {self.order_id}, Status: {self.order_status}, Items: [{items_titles}]"


class Invoice:
    """Generates the invoice for a customer's order."""

    def __init__(self, customer, shopping_cart, pricing_engine):
        self.invoice_number = None  # Initialize invoice number
        self.order_date = datetime.now().strftime("%Y-%m-%d")
        self.customer = customer
        self.shopping_cart = shopping_cart
        self.pricing_engine = pricing_engine
        self.items = len(shopping_cart.items)  # Count items
        self.total_price = self._calculate_total_price()

    def _calculate_total_price(self):
        total_price = 0
        for ebook in self.shopping_cart.items:
            total_price += self.pricing_engine.calculate_price(ebook, self.customer.is_loyalty_member, 1)
        return total_price

    def generate_invoice(self):
        print(f"Invoice for {self.customer.name}")
        print(f"Order Date: {self.order_date}")
        print("Items:")
        for ebook in self.shopping_cart.items:
            print(f"- {ebook}")
        print(f"Total: ${self.total_price:.2f}")

    def __str__(self):
        return f"Invoice for {self.customer.name} (Total: ${self.total_price:.2f})"


class PricingEngine:
    """Calculates the final price of e-books, applying discounts and VAT."""

    LOYALTY_DISCOUNT = 0.10  # 10% loyalty discount
    BULK_DISCOUNT = 0.20  # 20% bulk discount
    VAT_RATE = 0.08  # 8% VAT

    def calculate_price(self, ebook, is_loyalty_member, quantity):
        base_price = ebook.price * quantity

        if is_loyalty_member:
            discount_amount = base_price * self.LOYALTY_DISCOUNT
            base_price -= discount_amount

        if quantity >= 5:
            bulk_discount_amount = base_price * self.BULK_DISCOUNT
            base_price -= bulk_discount_amount

        total_price = base_price * (1 + self.VAT_RATE)
        return total_price

    def __str__(self):
        return f"Pricing Engine (Loyalty Discount: {self.LOYALTY_DISCOUNT * 100}%, Bulk Discount: {self.BULK_DISCOUNT * 100}%, VAT Rate: {self.VAT_RATE * 100}%)"


class ShoppingCart:
    """Manages the customer's shopping cart and order details."""

    def __init__(self):
        self._items = []
        self._order_date = None

    @property
    def items(self):
        return self._items

    @property
    def order_date(self):
        return self._order_date

    def add_item(self, ebook):
        self._items.append(ebook)

    def remove_item(self, ebook):
        self._items.remove(ebook)

    def update_quantity(self, ebook, new_quantity):
        for item in self._items:
            if item == ebook:
                self._items.remove(ebook)
                for _ in range(new_quantity - 1):  # Add back the desired quantity
                    self._items.append(ebook)
                break

    def place_order(self):
        self._order_date = datetime.now().strftime("%Y-%m-%d")
        return [item.title for item in self._items]

    def __str__(self):
        return f"Shopping Cart ({len(self._items)} items)"