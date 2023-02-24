from CapstoneProjects.resources.ResourcesForCoffeeMachine import MENU, resources
from prettytable import PrettyTable


table = PrettyTable()

print(MENU)

table.add_column("Beravage", ["espresso", "latte", "cappuccino"])
table.add_column("Water", [50, 200, 250])
table.add_column("Milk", [0, 150, 100])
table.add_column("Coffee", [18, 24, 24])


print(table)




