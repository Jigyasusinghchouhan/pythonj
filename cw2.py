up_down = ["D", "U", "D", "D", "U", "D", "D", "D", "U"]
position = 0

for move in up_down:
    if move == "U":
        position += 1
    else:
        position -= 1

print(":", position)
