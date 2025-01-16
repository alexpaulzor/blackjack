import random


class Card(object):
    """Represents a playing card"""
    # Ace => 1
    # 2 - 10 => 2 - 10
    # Jack => 11
    # Queen => 12
    # King => 13
    def __init__(self, number, suit):
        self._number = number
        self.suit = suit

    # The blackjack number value of this Card
    # Ace => 1
    # 2 - 10 => 2 - 10
    # Jack, Queen, King => 10
    @property
    def number(self):
        return min(self._number, 10)

    @property
    def is_ace(self):
        return self.number == 1

    def __str__(self):
        return f"{self.type}{self.suit}"

    # More human-readable translation for face cards
    @property
    def type(self):
        translations = {
            1: "A",
            11: "J",
            12: "Q",
            13: "K",
        }
        return translations.get(self.number, self.number)


class Shoe(object):
    """Represents a shoe (or collection of decks) of playing cards"""
    def __init__(self, decks=8):
        self._cards = []
        # Hearts, Clubs, Diamonds, Spades
        suits = ["H", "C", "D", "S"]
        for deck in range(1, decks):
            for number in range(1, 13):
                for suit in suits:
                    self._cards.append(Card(number, suit))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self._cards)
        self._undealt_cards = len(self._cards)

    # Get 2 cards
    def deal(self):
        return self.cards(2)

    # Get 1 card
    def hit(self):
        return self.cards(1)[0]

    # Get an Array of numcards Cards (and puts them at the end of the Shoe
    # [presuming they will be discarded])
    def cards(self, numcards=1):
        if numcards > self._undealt_cards:
            print("(shuffling shoe)")
            self.shuffle()
        cards = [self._cards.pop(0) for i in range(numcards)]
        self._cards += cards
        self._undealt_cards -= numcards
        return cards


class Hand(object):
    """A blackjack Hand"""
    def __init__(self, cards):
        if not isinstance(cards, list):
            raise RuntimeError(f"{cards=} is not list")
        self.cards = cards

    @property
    def is_busted(self):
        return self.sum > 21

    # Get the maximum non-busting sum from this Hand.
    @property
    def sum(self):
        hand_sum = self.soft_sum
        if self.has_ace:
            if hand_sum <= 10:
                hand_sum = hand_sum + 11
            else:
                hand_sum = hand_sum + 1

        return hand_sum

    # Get the sum of all cards that are not variable (i.e. not the first ace).
    @property
    def soft_sum(self):
        hand_sum = 0
        have_ace = False
        for card in self.cards:
            if card.is_ace and not have_ace:
                have_ace = True
            else:
                hand_sum = hand_sum + card.number
        return hand_sum

    @property
    def has_ace(self):
        for card in self.cards:
            if card.is_ace:
                return True
        return False

    @property
    def is_blackjack(self):
        return (self.size == 2 and self.sum == 21)

    @property
    def size(self):
        return len(self.cards)

    # Add one more Card to this Hand.
    def hit(self, card):
        self.cards.append(card)

    def __str__(self):
        output = ""
        for card in self.cards:
            output += f"{card} "
        output += f"=> {self.sum}"
        if self.is_blackjack:
            output += " Blackjack!"
        elif self.is_busted:
            output += " Busted!"
        return output


class DealerHand(Hand):
    def __init__(self, cards):
        super().__init__(cards)
        self.visible = False

    @property
    def upcard(self):
        return self.cards[0]

    def show(self):
        self.visible = True

    def __str__(self):
        if self.visible:
            return super().__str__()
        else:
            return f"{self.upcard} ??"


class BetterHand(Hand):
    def __init__(self, cards, bet=0):
        super().__init__(cards)
        self.bet = bet

    def __str__(self):
        return f"${self.bet} on " + super().__str__()

    @property
    def can_split(self):
        return (
            len(self.cards) == 2 and
            self.cards[0].number == self.cards[1].number)

    # Moves this hand's second card to a new hand and returns it.
    def split(self):
        otherHand = BetterHand([self.cards.pop(1)], self.bet)
        return otherHand
