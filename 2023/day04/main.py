def get_points(scratchcard):
    return 2**get_winning_amount(scratchcard) // 2

def get_winning_amount(scratchcard):
    winning_numbers, my_numbers = scratchcard
    number_of_winning_numbers = 0
    for number in my_numbers:
        if number in winning_numbers:
            number_of_winning_numbers += 1
    return number_of_winning_numbers

def amount_of_scratchcards(scratchcards):
    copies_of_card = [1 for _ in scratchcards]
    for card_number, scratchcard in enumerate(scratchcards):
        amount_winning = get_winning_amount(scratchcard)
        add_copies(copies_of_card, card_number, amount_winning)
    return copies_of_card

def add_copies(copies_of_card, card_number, amount_matching):
    copies_to_add = copies_of_card[card_number]
    for i in range(card_number + 1, card_number + 1 + amount_matching):
        copies_of_card[i] += copies_to_add

if __name__ == "__main__":
    import os
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    data = open(os.path.join(__location__, "input.txt"), "r").read()
    scratchcards = tuple(tuple(tuple(filter(lambda z: z != "", y.split(" "))) for y in x.split(": ")[1].split(" | ")) for x in data.split("\n"))

    for scratchcard in scratchcards:
        if len(scratchcard) != 2:
            print(len(scratchcard))
    
    print("Part 1:", sum([get_points(scratchcard) for scratchcard in scratchcards]))
    print("Part 2:", sum(amount_of_scratchcards(scratchcards)))