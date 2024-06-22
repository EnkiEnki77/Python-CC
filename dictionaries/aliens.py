# If we have multiple dictionaries all sharing the same kind of data that we'd like to store together we can store them
# in a list. This is called nesting.
alien_0 = {"color": "green", "speed": "slow", "points": "5"}
alien_1 = {"color": "yellow", "speed": "medium", "points": "10"}
alien_2 = {"color": "red", "speed": "fast", "points": "15"}

aliens = [alien_0, alien_1, alien_2]
print(aliens)

print("\n")
# More realistically we could start with an empty list and append objects to it dynamically
aliens = []

for alien_number in range(30):
    new_alien = {"color": "green", "speed": "slow", "points": "5"}
    aliens.append(new_alien)

print(*aliens[:3])
print(len(aliens))

print("\n")
# We can now modify each alien dictionary independently. 
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'

print(*aliens[:5], sep="\n")

# When storing multiple dictionaries in a list each one should have an identical structure so you can loop through the list
# and work with the dictionaries in the same way. 

