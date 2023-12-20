CARD_TYPES1 = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
CARD_TYPES2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
CARD_TYPES = CARD_TYPES2

def type_of_hand1(hand, card_types):
    card_counts = {card_type: 0 for card_type in card_types}

    for card in hand:
        card_counts[card] += 1

    counts = sorted(list(card_counts.values()), reverse=True)

    if counts[0] == 5:
        return 6
    elif counts[0] == 4:
        return 5
    elif counts[0] == 3 and counts[1] == 2:
        return 4
    elif counts[0] == 3:
        return 3
    elif counts[0] == 2 and counts[1] == 2:
        return 2
    elif counts[0] == 2:
        return 1
    else:
        return 0

def type_of_hand2(hand, card_types):
    card_counts = {card_type: 0 for card_type in card_types}

    for card in hand:
        card_counts[card] += 1

    jokers = card_counts["J"]
    del card_counts["J"]

    counts = sorted(list(card_counts.values()), reverse=True)

    if counts[0] + jokers == 5:
        return 6
    elif counts[0] + jokers == 4:
        return 5
    elif counts[0] + jokers == 3 and counts[1] == 2:
        return 4
    elif counts[0] + jokers == 3:
        return 3
    elif counts[0] + jokers == 2 and counts[1] == 2:
        return 2
    elif counts[0] + jokers == 2:
        return 1
    else:
        return 0
    
def hand_value(hand, card_types, type_of_hand_func):
    card_values = {key: value for value, key in enumerate(card_types)}

    value = 0
    
    for i, card in enumerate(reversed(hand)):
        value += card_values[card] * 10**(i*2)

    value += type_of_hand_func(hand, card_types) * 10**10

    return value

def total_winnings(hands, card_types, type_of_hand_func):
    sorted_hands = sorted(hands, key=lambda x: hand_value(x[0], card_types, type_of_hand_func))

    total = 0

    for index, hand in enumerate(sorted_hands):
        total += int(hand[1]) * (index + 1)

    return total

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()

    data = list(data.split("\n"))
    hands = list(x.split(" ") for x in data)

    print("Part 1:", total_winnings(hands, CARD_TYPES1, type_of_hand1))
    print("Part 2:", total_winnings(hands, CARD_TYPES2, type_of_hand2))
