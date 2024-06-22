squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# There are three functions helpful for finding the statistics of a list. min, max, and sum
print(min(squares))
print(max(squares))
print(sum(squares))