rivers = {
    "nile": "egypt",
    "missisippi": "usa",
    "amazon": "Brazil"
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in rivers:
    print(river)

for city in rivers.values():
    print(city)