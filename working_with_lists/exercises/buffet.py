buffet_foods = ("pizza", "wings", "mac", "beans", "broccoli")

print(*buffet_foods, sep="\n")

# tuples are immutable, so if you want to alter them you need to create a whole new tuple. 
buffet_foods =  ("pizza", "wings", "cookie", "beans", "broccoli")

print(*buffet_foods, sep="\n")