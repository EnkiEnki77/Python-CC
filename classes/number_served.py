from restaurants import Restaurant

restaurant = Restaurant('restaurant', 'tacos')

print(restaurant.number_served)
restaurant.number_served = 24
print(restaurant.number_served)

restaurant.increment_number_served(32)
restaurant.set_number_served(54)
