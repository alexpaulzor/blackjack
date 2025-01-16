import math
from planet.blackjack.models import (
    DealerHand,
    BetterHand,
)
from planet.blackjack.strategy import basic_strategy
from planet.blackjack.utils import string_input, integer_input


class Player(object):
    """Base for all players"""
    def __init__(self, shoe, name="Player"):
        self.shoe = shoe
        self.name = name

    # Plays this Player's turn
    def play(self):
        for hand in self.hands:
            self.play_hand(hand)

    # Required (but not implemented in Player) helper to Player::play()
    def play_hand(self, hand):
        raise NotImplementedError()

    # Begin a new round.
    # Must be called on every Player before Player::play() is called.
    def new_round(self):
        raise NotImplementedError()

    def hit(self, hand):
        hand.hit(self.shoe.hit())

    def __str__(self):
        return self.name

    def print_status(self):
        for hand in self.hands:
            print(f"{self}: {hand}")


class Dealer(Player):
    """The blood-sucking dealer"""

    def __init__(self, shoe, name="Dealer"):
        super().__init__(shoe, name)

    @property
    def upcard(self):
        return self.hand.upcard

    # The dealer only has one hand.
    @property
    def hand(self):
        return self.hands[0]

    def new_round(self):
        self.highScore = 0
        self.hands = [DealerHand(self.shoe.deal())]

    # Let the dealer know what other players have scored, so he knows when he
    # can stop hitting.
    def notify_hand(self, hand):
        if not hand.is_busted and hand.sum > self.highScore:
            self.highScore = hand.sum

    # Robotic strategy -- if less than 17, dealer must hit.
    def play_hand(self, hand):
        hand.show()
        while True:
            if hand.sum < 17 and hand.sum <= self.highScore:
                print(f"{self}: {hand} > Hit")
                self.hit(hand)
            elif hand.sum <= 21:
                print(f"{self}: {hand} > Stand")
                break
            else:
                break
        print(f"{self}: {hand}")


class Better(Player):
    """A player that is not the dealer"""
    def __init__(self, shoe, dealer, money=1000.0, name=""):
        super().__init__(shoe, name)
        self.dealer = dealer
        self.money = money

    @property
    def is_bankrupt(self):
        return self.money <= 0

    def buy_in(self, money):
        self.money += money

    def can_afford(self, money):
        return self.money >= money

    def __str__(self):
        return f"{self.name} (${self.money})"

    def new_round(self):
        self.hands = []
        if self.is_bankrupt:
            return
        bet = self.get_bet()
        print(f"{self} bets ${bet}")
        self.money -= bet
        self.hands = [BetterHand(self.shoe.deal(), bet)]

    def get_bet(self):
        return max(math.floor(self.money / 4), 1)

    def end_round(self):
        for hand in self.hands:
            self.reward_hand(hand)

    # Pay the player what they've won with hand.
    def reward_hand(self, hand):
        if hand.is_busted:
            print(f"{self}: {hand} > Lose ${hand.bet}")
        elif (self.dealer.hand.is_busted or hand.sum > self.dealer.hand.sum
                or hand.is_blackjack and not self.dealer.hand.is_blackjack):
            # Win, give player twice their bet (1 because they get their
            # bet back, 1 because they won money from the house)
            print(f"{self}: {hand} > Win ${hand.bet}")
            self.money += hand.bet * 2
        elif hand.sum == self.dealer.hand.sum:
            # Push, return the player's bet.
            print(f"{self}: {hand} > Push")
            self.money += hand.bet
        else:
            print(f"{self}: {hand} > Lose ${hand.bet}")

    def split(self, hand):
        if not self.can_afford(hand.bet):
            return

        self.money -= hand.bet
        newhand = hand.split()
        self.hit(hand)
        self.hit(newhand)
        self.hands.append(newhand)

    def double_down(self, hand):
        if not self.can_afford(hand.bet):
            return

        self.money -= hand.bet
        hand.bet *= 2
        self.hit(hand)

    def can_double_down(self, hand):
        return (hand.size == 2 and self.can_afford(hand.bet))

    def can_split(self, hand):
        return (hand.can_split and self.can_afford(hand.bet))

    # Compute basic strategy (as per wikipedia)
    def basic_strategy(self, hand):
        return basic_strategy(
            hand, self.dealer.upcard.number,
            self.can_split(hand), self.can_double_down(hand))


# A human player
class Human(Better):
    def get_bet(self):
        default = super().get_bet()
        return integer_input(
            f"{self}: bet [{default}] > ",
            f"Invalid input, please enter an integer between 1 and {self.money}",
            default, 1, self.money)

    # Plays the hand until the user stays or busts.
    # Will modify self.hands (indirectly) if the user splits; self.money if the
    # user doubles-down.
    def play_hand(self, hand):
        options = {
            "hit": ["hit", "h", "!"],
            "stand": ["stand", "st", "stay", "stick"],
            "split": ["split", "sp", "/"],
            "double_down": ["doubledown", "dd", "d", "2", "*", "+"],
            "help": ["help", "h", "?"],
        }

        playing = True
        while playing and not hand.is_busted:
            allowed_options = options["stand"] + options["hit"] + options["help"]
            prompt = f"{options['stand'][0]}/{options['hit'][0]}"

            if hand.size == 2 and self.can_afford(hand.bet):
                allowed_options += options['double_down']
                prompt += f"/{options['double_down'][0]}"

            if hand.can_split and self.can_afford(hand.bet):
                allowed_options += options['split']
                prompt += f"/{options['split'][0]}"

            default = options[self.basic_strategy(hand)][0]

            choice = string_input(
                f"{self}: {hand} >> {prompt} [{default}] > ",
                allowed_options, "Invalid choice. Try \"help\".", default)

            if choice in options['stand']:
                playing = False
            elif choice in options['hit']:
                self.hit(hand)
            elif choice in options['split'] and self.can_split(hand):
                self.split(hand)
            elif choice in options['double_down'] and self.can_double_down(hand):
                self.double_down(hand)
                playing = False
            else:
                self.show_help(options)
        self.dealer.notify_hand(hand)
        print(f"{self}: {hand}")

    def show_help(self, options):
        print("Stand: " + options['stand'].join(", "))
        print("Hit: " + options['hit'].join(", "))
        print("Double down: " + options['double_down'].join(", "))
        print("Split: " + options['split'].join(", "))
        print("This help: " + options['help'].join(", "))


# A computer AI that just does basic strategy.
class Computer(Better):
    def play_hand(self, hand):
        playing = True
        while playing and not hand.is_busted:
            strategy = self.basic_strategy(hand)

            if strategy == 'hit':
                print(f"{self}: {hand} > Hit")
                self.hit(hand)
            elif strategy == 'split' and self.can_split(hand):
                print(f"{self}: {hand} > Split")
                self.split(hand)
            elif strategy == 'double_down' and self.can_double_down(hand):
                print(f"{self}: {hand} > Double down")
                self.double_down(hand)
                playing = False
            else:     # stand
                print(f"{self}: {hand} > Stand")
                playing = False
        self.dealer.notify_hand(hand)
        print(f"{self}: {hand}")

    def __str__(self):
        return "[AI] " + super().__str__()
