# Given a function that generates perfectly random numbers between 1 and k (inclusive),
# where k is an input, write a function that shuffles a deck of cards represented as an
# array using only swaps.

# It should run in O(N) time.

# Hint: Make sure each one of the 52! permutations of the deck is equally likely.


from random import randint


def get_perfectly_random(k):
    return randint(0, k)


def swap(deck, new_pos, old_pos):
    temp = deck[new_pos]
    deck[new_pos] = deck[old_pos]
    deck[old_pos] = temp


def shuffle_deck(deck):
    for old_pos in deck:
        # Swap the current card with a random card anywhere from itself until the end of the deck
        new_pos = old_pos + get_perfectly_random(len(deck) - old_pos - 1)
        swap(deck, new_pos, old_pos)

    return deck


# Driver code
NUM_CARDS = 52
deck = [card for card in range(NUM_CARDS)]
print(shuffle_deck(deck))