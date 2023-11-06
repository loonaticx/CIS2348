class ItemToPurchase:

    def __init__(self, item_name: str = "none", item_price: float = 0.0,
                 item_quantity: int = 0, item_description: str = 'none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    # Since price+qty can change after init, we may need to recalculate the price when called for.
    @property
    def total_cost(self):
        return int(self.item_quantity * self.item_price)

    def print_item_cost(self):
        return print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${self.total_cost}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    def __init__(self, customer_name: str = 'none', current_date: str = "January 1, 2016", cart_items: list = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def _baseinfo(self):
        """
        John Doe's Shopping Cart - February 1, 2016
        """
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")

    def add_item(self, item_to_purchase: ItemToPurchase):
        """
        Adds an item to cart_items list.
        """
        self.cart_items.append(item_to_purchase)

    def remove_item(self, itemName: str):
        for cart_item in self.cart_items:
            if cart_item.item_name == itemName:
                self.cart_items.pop(self.cart_items.index(cart_item))
                print()
                return
        print(f"Item not found in cart. Nothing removed.\n")

    def modify_item(self, item: ItemToPurchase):
        """
        Modifies an item's quantity
        """
        item_name = item.item_name
        qty = item.item_quantity
        for cart_item in self.cart_items:
            if cart_item.item_name == item_name:
                cart_item.item_quantity = qty
                print()
                return
        print(f"Item not found in cart. Nothing modified.\n")

    def get_num_items_in_cart(self):
        total_items = 0
        for item_entry in self.cart_items:
            total_items += item_entry.item_quantity
        return total_items

    def get_cost_of_cart(self):
        item_cost = 0
        for item_entry in self.cart_items:
            item_cost += item_entry.total_cost
        return int(item_cost)

    def print_total(self):
        """
        Outputs total of objects in cart.
        """

        self._baseinfo()
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        print()
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item_entry in self.cart_items:
                item_entry.print_item_cost()

        print()
        print(f"Total: ${self.get_cost_of_cart()}\n")

    def print_descriptions(self):
        """
        Outputs each item's description.
        """
        self._baseinfo()
        print()
        print("Item Descriptions")
        for item_entry in self.cart_items:
            item_entry.print_item_description()


class ShoppingMenu:

    def __init__(self, shopping_cart: ShoppingCart):
        self.cart = shopping_cart

    def print_menu(self, show_full=True):
        if show_full:
            print("MENU")
            print("a - Add item to cart", end = '')
            print()
            print("r - Remove item from cart")
            print("c - Change item quantity")
            print("i - Output items' descriptions")
            print("o - Output shopping cart")
            print("q - Quit")
            print()
        return str(input("Choose an option:\n"))

    def print_shopping_cart(self):
        print("OUTPUT SHOPPING CART")
        self.cart.print_total()

    def print_cart_desc(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        self.cart.print_descriptions()
        print()

    def add_item(self):
        print("ADD ITEM TO CART")
        item_name = str(input("Enter the item name:\n"))
        item_desc = str(input("Enter the item description:\n"))
        item_price = float(input("Enter the item price:\n"))
        item_qty = int(input("Enter the item quantity:\n"))
        print()
        new_item = ItemToPurchase(item_name, item_price, item_qty, item_desc)
        self.cart.cart_items.append(new_item)

    def remove_item(self):
        print("REMOVE ITEM FROM CART")
        item = str(input("Enter name of item to remove:\n"))
        self.cart.remove_item(item)

    def change_item_qty(self):
        print("CHANGE ITEM QUANTITY")
        item_name = str(input("Enter the item name:\n"))
        qty = int(input("Enter the new quantity:\n"))
        self.cart.modify_item(ItemToPurchase(item_name = item_name, item_quantity = qty))


if __name__ == "__main__":
    custName = str(input("Enter customer's name:\n"))
    todaysDate = str(input("Enter today's date:\n"))
    print()
    print(f"Customer name: {custName}")
    print(f"Today's date: {todaysDate}")
    print()
    shoppingCart = ShoppingCart(custName, todaysDate)
    menu = ShoppingMenu(shoppingCart)
    wannaExit = False
    show_full = True
    while not wannaExit:
        option = menu.print_menu(show_full)
        show_full = True
        if option == "a":
            menu.add_item()
        elif option == "r":
            menu.remove_item()
        elif option == "c":
            menu.change_item_qty()
        elif option == "i":
            menu.print_cart_desc()
        elif option == "o":
            menu.print_shopping_cart()
        elif option == "q":
            wannaExit = True
        else:
            show_full = False
