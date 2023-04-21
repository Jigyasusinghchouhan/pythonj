Doremon = [75, 10, 34, 70, 90]
Shinchan = [56, 89, 12, 90, 45]


def find_winner(Doremon, Shinchan):
    Doremon_wins = 0
    Shinchan_wins = 0
    for i in range(len(Doremon)):
        if Doremon[i] > Shinchan[i]:
            Doremon_wins += 1
        elif Shinchan[i] > Doremon[i]:
            Shinchan_wins += 1
    if Doremon_wins > Shinchan_wins:
        return "Doremon", Doremon_wins
    elif Shinchan_wins > Doremon_wins:
        return "Shinchan", Shinchan_wins
    else:
        return "tie", Doremon_wins


result = find_winner(Doremon, Shinchan)
print("", result[0], "", result[1], "")
