sandwich_orders = ['blt', 'cold cut combo', 'pastrami', 'meatball sub', 'pastrami', 'steak and cheese', 'pastrami']
finished_sandwhiches = []

print(sandwich_orders)
print("Sorry, we're out of pastrami today\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwhich = sandwich_orders.pop()
    print(f"I made your {sandwhich}")

    finished_sandwhiches.append(sandwhich)

print("\nSandwhiches finsihed:")
print(*finished_sandwhiches, sep="\n")