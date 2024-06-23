sandwich_orders = ['blt', 'cold cut combo', 'meatball sub', 'steak and cheese']
finished_sandwhiches = []

while sandwich_orders:
    sandwhich = sandwich_orders.pop()
    print(f"I made your {sandwhich}")

    finished_sandwhiches.append(sandwhich)

print("\nSandwhiches finsihed:")
print(*finished_sandwhiches, sep="\n")