# Quickstart

    python3 main.py --help

    Usage: main.py [OPTIONS]

    Options:
      -a, --ai TEXT             Specify an AI player by name (with optional =xyz
                                buyin amount, default $1000). Can be repeated for
                                multiple AIs
      -h, --player TEXT         Specify a human player by name (with optional =xyz
                                buyin amount, default $1000). Can be repeated for
                                multiple players
      -r, --num-rounds INTEGER  Automatically play this number of rounds
      -R, --autoplay            Automatically play until all players are bankrupt
      -i, --interactive         Continue playing interactively after -r or -R
      --help                    Show this message and exit.


## Dependencies

    pip3 install -r requirements.txt


## Testing

    python3 -m pytest test/

# Rules of the Game

See [wikipedia](https://en.wikipedia.org/wiki/Blackjack) for more details.

tl;dr Blackjack is a card game where some number of betting players try to beat
the dealer. Each player starts by placing a bet, and then is dealt two cards
face-up. The dealer is dealt two cards, but one is not visible until all betting
players have finished their hands.

The goal is for all cards in a hand to total as close to 21 as possible without
going over (aka "busting").
Numeric cards are worth their number.
Face cards are worth 10.
Aces are worth 11, or 1 if counting as 11 would cause the hand to bust.

One by one, each player has an opportunity to receive more cards ("hit") or can
choose to "stay."
Once all players have finished receiving their cards, the dealer flips over
their face-down card and "hits" until their hand totals 17 or more.

Then, each player whose total is 21 or less but greater than the dealer (or the
dealer busts) wins an amount equal to their bet.
Any player who busts or whose total is less than the dealer forfeits their bet.
If a player's total equals the dealer's, it is a "push" (aka tie) and the
player's bet is returned.

There are some other cases ("split" or "double down") whose details can be
read on wikipedia.

# Simulation

The purpose of this interview exercise is to implement a simulation of a
statistically-significant number of games and produce metrics describing the
expected results after a specific number of hands in each game.

This repo already contains an implementation of the basic strategy described
on wikipedia, and there are `Computer` betters that faithfully execute the
basic strategy for each hand.

See `sim.py` for development TODOs.
