cards = {
    "A": 10,
    "K": 10,
    "Q": 10,
    "J": 10,
    "T": 10,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}

def f(player1, player2):
    sum1 = 0
    for item in player1:
        sum1 += cards[item]
        
    sum2 = 0
    for item2 in player2:
        sum2 += cards[item2]
        
    if sum1 > sum2:
        return True
    else:
        return False
