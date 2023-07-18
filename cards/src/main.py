from random import choice
from cards import Card, FrenchDeck
from colorama import Fore, Style


def spades_high(card: Card) -> int:
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


def main():
    deck = FrenchDeck()
    # These are the thing we enabled
    print(
        f"{Style.BRIGHT}{Fore.GREEN}Length of the deck:{Style.RESET_ALL}               {len(deck)}"
    )
    print(
        f"{Style.BRIGHT}{Fore.BLUE}Top of the deck:{Style.RESET_ALL}                  {deck[0]}"
    )
    print(
        f"{Style.BRIGHT}{Fore.GREEN}Bottom of the deck:{Style.RESET_ALL}               {deck[-1]}"
    )
    # And these are the thing we got as a result
    print(
        f"{Style.BRIGHT}{Fore.BLUE}Random card picked from the deck:{Style.RESET_ALL} {choice(deck)}"
    )
    print(
        f"{Style.BRIGHT}{Fore.GREEN}All the aces from the deck:{Style.RESET_ALL}       {deck[12::13]}"
    )
    print(
        f"{Style.BRIGHT}{Fore.BLUE}The top five card on the deck in the reverse order are: {Style.RESET_ALL}"
    )
    for card in reversed(deck[:5]):
        print(f"                                  - {card}")
    print(
        f'{Style.BRIGHT}{Fore.GREEN}Is Queen of Hearts in the deck:{Style.RESET_ALL}   {Card("Q", "hearts") in deck}'
    )
    print(
        f"{Style.BRIGHT}{Fore.BLUE}Sorted Deck:                      {Style.RESET_ALL}",
        end="",
    )
    for card in sorted(deck, key=spades_high):
        print(card, end=" ")
    