from planet.blackjack.blackjack import Blackjack


def sim_game(
    ai=["AI1", "AI2", "AI3", "AI4", "AI5"],
    num_hands=100,
):
    game = Blackjack()

    for p in ai:
        buyin = 1000
        if '=' in p:
            p, buyin = p.rsplit('=', 1)
            buyin = int(buyin)
        game.add_computer(p, buyin)

    for hand in range(num_hands):
        game.new_round()


def sim_games(
    ai=["AI1", "AI2", "AI3", "AI4", "AI5"],
    num_hands=100,
    num_games=1000,
):
    for gamenum in range(num_games):
        sim_game(ai, num_hands)
        print(f"Game {gamenum} complete")

    # TODO: After simulating 1000 games of 100 hands each with 5 AI players,
    # 1. What is the average remaining money for each player, ranked
    #    most-successful to least (i.e. not grouped by name, but instead sorted
    #    by remaining money)
    # 2. What is the average number of non-bankrupt players at the end of each
    #    hand
    #    i.e. after hand 1, on average there will still be 5 players with
    #    non-zero money, after hand 10, there will be 4 remaining players, etc.
    # 3. (bonus) What is the standard distribution of the average given in
    #    item 1
    # 4. (bonus) What is the standard distribution of the averages given in
    #    item 2
    # 5. (bonus) Write unit tests for (and fix!) any bug(s) you encounter
    # 6. (bonus) Produce a chart depicting relevant measurements


if __name__ == '__main__':
    sim_game()
