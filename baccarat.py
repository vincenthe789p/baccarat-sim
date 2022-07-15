# This is a python file to show how the game works
import random
VALUE_MAP = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 0, 'J': 0, 'Q': 0, 'K': 0}
OUTCOME = ['Player wins', 'Banker wins', 'Tie']
# Inclusive range function
irange = lambda start, end: range(start, end + 1)

def random_pick(deck):
    return deck.pop(random.randrange(len(deck)))

def compute_score(hand):
    """Compute the score of a hand"""
    total_value = 0
    for card in hand:
        total_value += VALUE_MAP[card]
    return total_value % 10

def play():
    """Returns the winner"""
    DECK = ['A','A','A','A', 'K', 'K', 'K', 'K', 'Q', 'Q', 'Q', 'Q', 'J', 'J', 'J', 'J']
    for i in range(2, 11):
        for j in range(4):
            DECK.append(str(i))
    player_hand = [
        random_pick(DECK),
        random_pick(DECK)
    ]
    banker_hand = [
        random_pick(DECK),
        random_pick(DECK)
    ]

    player_score = compute_score(player_hand)
    banker_score = compute_score(banker_hand)

    # print('Player has cards:\t' + player_hand[0] + '\t' + player_hand[1])
    # print('Player has score of\t' + str(player_score))
    # print('Banker has cards:\t' + banker_hand[0] + '\t' + banker_hand[1])
    # print('Banker has score of\t' + str(banker_score))

    # Natural
    if player_score in [8, 9] or banker_score in [8, 9]:
        if player_score != banker_score:
            return OUTCOME[banker_score > player_score]
        else:
            return OUTCOME[2]

    # Player has low score
    if player_score in irange(0, 5):
        # Player get's a third card
        player_hand.append(random_pick(DECK))
        player_third = compute_score([player_hand[2]])
        # print('Player gets a third card:\t' + player_hand[2])

        # Determine if banker needs a third card
        if (banker_score == 6 and player_third in [6, 7]) or \
           (banker_score == 5 and player_third in irange(4, 7)) or \
           (banker_score == 4 and player_third in irange(2, 7)) or \
           (banker_score == 3 and player_third != 8) or \
           (banker_score in [0, 1, 2]):
            banker_hand.append(random_pick(DECK))
            # print('Banker gets a third card:\t' + banker_hand[2])

    elif player_score in [6, 7]:
        if banker_score in irange(0, 5):
            banker_hand.append(random_pick(DECK))
            # print('Banker gets a third card:\t' + banker_hand[2])

    # Compute the scores again and return the outcome
    player_score = compute_score(player_hand)
    banker_score = compute_score(banker_hand)

    # print('Player has final score of\t' + str(player_score))
    # print('Banker has final score of\t' + str(banker_score))

    if player_score != banker_score:
        return OUTCOME[banker_score > player_score]
    else:
        return OUTCOME[2]

