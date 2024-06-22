guest_list = ["Gpa", "Vessel", "Johnny Depp"]

print(f"Im sorry to hear you cant make it {guest_list[1]}")

i = guest_list.index("Vessel")

# print(i)

# This is how to replace an item in a list using slicing
guest_list = guest_list[:i]+["Nothing, Nowhere"]+guest_list[i+1:]

for name in guest_list:
    print(f"Hey {name}, id like to invite you to dinner.")

print("It turns out there's a bigger table, so we'll be inviting additional guests!")

guest_list.insert(0, "Brad Pitt")
guest_list.insert(2, "Dragon Lady")
guest_list.append("Batman")

for name in guest_list:
    print(f"\nHey {name}, id like to invite you to dinner.")