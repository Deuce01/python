class InventorySystem:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

    def remove_item(self, item, quantity):
        if item in self.inventory:
            if self.inventory[item] >= quantity:
                self.inventory[item] -= quantity
                if self.inventory[item] == 0:
                    del self.inventory[item]
            else:
                print(f"Not enough {item} in stock.")
        else:
            print(f"{item} not found in inventory.")

    def display_inventory(self):
        print("Current Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")

# Example usage:
inventory_system = InventorySystem()

inventory_system.add_item("Apples", 50)
inventory_system.add_item("Bananas", 30)
inventory_system.add_item("Oranges", 40)

inventory_system.display_inventory()

inventory_system.remove_item("Apples", 20)
inventory_system.remove_item("Bananas", 40)

inventory_system.display_inventory()
