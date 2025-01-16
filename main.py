#!/usr/bin/env python3

from planet.blackjack.blackjack import blackjack_main
import click

# Simulates Blackjack

# USAGE: python3 main.py
# The Blackjack > prompt is the main menu.
# Try typing "help" to see what you can do from there.


@click.command
@click.option(
    "--ai", "-a", multiple=True,
    help=(
        "Specify an AI player by name (with optional =xyz buyin amount, "
        "default $1000). Can be repeated for multiple AIs"
    )
)
@click.option(
    "--player", "-h", multiple=True,
    help=(
        "Specify a human player by name (with optional =xyz buyin amount, "
        "default $1000). Can be repeated for multiple players"
    )
)
@click.option(
    "--num-rounds", "-r", type=int, default=None,
    help="Automatically play this number of rounds")
@click.option(
    "--autoplay", "-R", is_flag=True,
    help="Automatically play until all players are bankrupt")
@click.option(
    "--interactive", "-i", is_flag=True,
    help="Continue playing interactively after -r or -R")
def main(ai, player, num_rounds, autoplay, interactive):
    blackjack_main(ai, player, num_rounds, autoplay, interactive)


if __name__ == '__main__':
    main()


# TODO: write unit tests for basic scenarios
# TODO: create simulation wrapper that can simulate a given scenario (number of
#       players, buy-in amounts, max rounds or exit conditions) a given number
#       of trials and produce a report on the expected result of a scenario
#       (expected money for each player after a given number of rounds, or the
#       expected number of rounds where another player will run out of money
#       until no players are left)
# TODO (bonus): implement a variant of the AI that can count cards
