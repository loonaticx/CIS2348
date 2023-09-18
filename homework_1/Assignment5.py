"""
Erica Miller
2031854
"""
# Define the menu of automotive services and their corresponding costs
shop_menu = {
    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7,
    "Car wax": 12,
}

# Output the menu
print("Davy's auto shop services")
for service, cost in shop_menu.items():
    print(f"{service} -- ${cost}")

# Prompt the user for two services
print("\nSelect first service:")
service1 = input()
print("Select second service:")
service2 = input()

# Output an invoice for the services selected
print("\nDavy's auto shop invoice\n")
total_cost = 0

if service1 in shop_menu:
    print(f"Service 1: {service1}, ${shop_menu[service1]}")
    total_cost += shop_menu[service1]
else:
    print("Service 1: No service")

if service2 in shop_menu:
    print(f"Service 2: {service2}, ${shop_menu[service2]}")
    total_cost += shop_menu[service2]
else:
    print("Service 2: No service")

print(f"\nTotal: ${total_cost}")
