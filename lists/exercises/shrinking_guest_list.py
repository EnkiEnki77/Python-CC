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

print("\n Unfortunately we can only invite two people after all.")

guest_list_slice = guest_list[:]
guest_list_slice.reverse()

print(guest_list)
for name in guest_list_slice:
    if len(guest_list) > 2:
        uninvited_guest = guest_list.pop()
        print(f"Sory {uninvited_guest}, you suck dick.")
    else:
        print(f"{name} youre still invited, you eat mad pussy.")



