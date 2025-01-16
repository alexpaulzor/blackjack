#!/usr/bin/env python3

import itertools
from planet.blackjack.models import (
    Shoe,
)
from planet.blackjack.player import (
    Dealer,
    Human,
    Computer,
)
from planet.blackjack.utils import string_input, integer_input

# Simulates Blackjack

# USAGE: python3 blackjack.py
# The Blackjack > prompt is the main menu.
# Try typing "help" to see what you can do from there.


# Simulates Blackjack
class Blackjack(object):
    def __init__(self, num_decks=8, shoe=None):
        self.betters = {}
        if not shoe:
            shoe = Shoe(num_decks)
        self.shoe = shoe
        self.dealer = Dealer(self.shoe)
        self.round = 1

    def add_player(self, name=None, money=None):
        if not name:
            name = string_input("Player name > ")
        if name in self.betters or name == self.dealer.name:
            print(f"There is already a player named {name}. Try \"listplayers\".")
            return
        if not money:
            money = integer_input(
                "Buy in amount [1000] > ",
                "Invalid input, please enter a positive integer.", 1000, 1)
        self.betters[name] = Human(self.shoe, self.dealer, money, name)
        print(f"{self.betters[name]} added.")

    def add_computer(self, name=None, money=None):
        if not name:
            name = string_input("AI name > ")
        if name in self.betters or name == self.dealer.name:
            print(f"There is already a player named {name}. Try \"listplayers\".")
            return
        if not money:
            money = integer_input(
                "Buy in amount [1000] > ",
                "Invalid input, please enter a positive integer.", 1000, 1)
        self.betters[name] = Computer(self.shoe, self.dealer, money, name)
        print(f"{self.betters[name]} added.")

    def remove_player(self):
        name = string_input("Player name > ")
        if name not in self.betters:
            print(f"There is no betting player named {name}. Try \"listplayers\".")
            return
        print(f"Cashed {name} out with ${self.betters[name].money}.")
        del self.betters[name]

    def buy_in(self):
        name = string_input("Player name > ")
        if name not in self.betters:
            print(f"There is no betting player named {name}. Try \"listplayers\".")
            return

        money = integer_input(
            "Buy in amount [1000] > ",
            "Invalid input, please enter a positive integer.", 1000, 1)
        self.betters[name].buy_in(money)
        print(f"Added ${money} to {self.betters[name]}")

    def new_round(self):
        if not self.betters:
            print("No players.")
            return
        print()
        print("-" * 20 + f" Round {self.round} " + "-" * 20)
        for name, player in self.betters.items():
            player.new_round()
        self.dealer.new_round()
        print("-" * 10 + f" Dealing Round {self.round} " + "-" * 10)
        self.show_table()
        for name, player in self.betters.items():
            print()
            print("-" * 5 + f" {player}'s turn " + "-" * 5)
            player.play()
        print()
        print("-" * 10 + " Dealer's turn " + "-" * 10)
        self.dealer.play()
        print()
        print("-" * 20 + f" Round {self.round} Result " + "-" * 20)
        self.dealer.print_status()
        for name, player in self.betters.items():
            player.end_round()
        print()
        self.round += 1

    @property
    def active_betters(self):
        return [b for b in self.betters.values() if b.money > 0]

    def play_rounds(self, num_rounds=None):
        while self.active_betters and (num_rounds is None or num_rounds > 0):
            self.new_round()
            if num_rounds is not None:
                num_rounds -= 1
        if not self.active_betters:
            print("All players are bankrupt")

    def show_table(self):
        self.dealer.print_status()
        for name, player in self.betters.items():
            player.print_status()

    def play(self):
        playing = True
        while playing:
            options = {
                'quit': ["quit", "q", "exit", "e"],
                'add': ["addplayer", "add", "a", "+"],
                'computer': ["addcomputer", "computer", "comp", "ai"],
                'remove': ["removeplayer", "remove", "r", "-"],
                'buy': ["buyin", "buy", "b", "money", "m", "$"],
                'play': ["play", "p"],
                'list': ["listplayers", "listplayer", "list", "l", "showplayers", "showplayer", "show", "s"],
                'help': ["help", "h", "usage", "u", "?"],
            }

            again = string_input(
                "Blackjack [play] > ",
                itertools.chain(*options.values()),
                "Invalid input. Try \"help\".", "play")

            if again in options['quit']:
                playing = False
            elif again in options['add']:
                self.add_player()
            elif again in options['computer']:
                self.add_computer()
            elif again in options['remove']:
                self.remove_player()
            elif again in options['buy']:
                self.buy_in()
            elif again in options['play']:
                self.new_round()
            elif again in options['list']:
                self.list_players()
            elif again in options['help']:
                self.show_help(options)
        self.list_players()

    def show_help(self, options):
        print()
        print("Add a player: " + ", ".join(options['add']))
        print("Add a computer player: " + ", ".join(options['computer']))
        print("Play a round: " + ", ".join(options['play']))
        print("List players: " + ", ".join(options['list']))
        print(
            "Buy in (add more money to player): " + ", ".join(options['buy']))
        print("Remove player: " + ", ".join(options['remove']))
        print("Quit: " + ", ".join(options['quit']))
        print("This help: " + ", ".join(options['help']))
        print()

    def list_players(self):
        print()
        for name, player in self.betters.items():
            print(player)
        print()


def blackjack_main(
        ai=None, player=None, num_rounds=None, autoplay=False,
        interactive=False, game=None):
    if not ai:
        ai = []
    if not player:
        player = []
    if not game:
        game = Blackjack()

    for p in player:
        buyin = 1000
        if '=' in p:
            p, buyin = p.rsplit('=', 1)
            buyin = int(buyin)
        game.add_player(p, buyin)
    for p in ai:
        buyin = 1000
        if '=' in p:
            p, buyin = p.rsplit('=', 1)
            buyin = int(buyin)
        game.add_computer(p, buyin)

    if num_rounds:
        game.play_rounds(num_rounds)
    if autoplay:
        game.play_rounds()
    if autoplay or num_rounds and not interactive:
        game.list_players()
    else:
        game.play()

    return game
