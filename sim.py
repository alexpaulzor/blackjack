from planet.blackjack.blackjack import Blackjack


def sim_game(
    ai=["AI1", "AI2", "AI3", "AI4", "AI5"],
    num_rounds=100,
):
    game = Blackjack()

    for p in ai:
        buyin = 1000
        if '=' in p:
            p, buyin = p.rsplit('=', 1)
            buyin = int(buyin)
        game.add_computer(p, buyin)

    for roundno in range(num_rounds):
        game.new_round()


def sim_games(
    ai=["AI1", "AI2", "AI3", "AI4", "AI5"],
    num_rounds=2,  # TODO: update to 100
    num_games=1,  # TODO: update to 1000
):
    for gamenum in range(num_games):
        sim_game(ai, num_rounds)
        print(f"Game {gamenum} complete")

    # TODO: After simulating 1000 games of 100 rounds each with 5 AI players,
    # 1. What is the average remaining money for each player, ranked
    #    most-successful to least (i.e. not grouped by name, but instead sorted
    #    by remaining money)
    # 2. What is the average number of non-bankrupt players at the end of each
    #    round
    #    i.e. after round 1, on average there will still be 5 players with
    #    non-zero money, after round 10, there will be 4 remaining players, etc.
    # 3. Write unit tests for (and fix!) any bug(s) you encounter
    # 4. (bonus) What is the standard distribution of the average given in
    #    item 1
    # 5. (bonus) What is the standard distribution of the averages given in
    #    item 2
    # 6. (bonus) Produce a chart depicting relevant measurements


if __name__ == '__main__':
    sim_games()
