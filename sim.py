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
    #    most-successful to least?
    #    i.e. not grouped by name, but instead sorted by remaining money.
    #    A concrete (simplified) example...suppose:
    #       After 100 rounds in game 0 with two AIs, the standing is:
    #           AI1: $500
    #           AI2: $250
    #       After 100 rounds in game 1 with two AIs, the standing is:
    #           AI1: $100
    #           AI2: $600
    #       The expected average by rank would be:
    #           ($500 + $600) / 2 = $550
    #           ($250 + $100) / 2 = $175
    #       And so the expected output would be a list whose length equals
    #           the number of players: [550, 175]

    # 2. Write unit tests for (and fix!) any bug(s) you encounter

    # 3. What is the average number of non-bankrupt players at the end of each
    #    round?
    #    i.e. after round 1, on average there will still be 5 players with
    #    non-zero money, after round 10, there will be 4 remaining players,
    #    etc.
    #    A concrete (simplified) example...suppose:
    #       Over the course of two games with four rounds and three AIs:
    #           Game 0: AI1 goes bankrupt after round 1, AI2 goes bankrupt
    #                   after round 3
    #           Game 1: AI3 goes bankrupt after round 1, AI1 and AI2 go
    #                   bankrupt after round 2
    #       Meaning that for each round the remaining players were:
    #           Round   Game 0 Players      Game 1 Players      Average
    #           0       3 (AI1, AI2, AI3)   3 (AI1, AI2, AI3)   3
    #           1       2 (AI2, AI3)        2 (AI1, AI2)        2
    #           2       2 (AI2, AI3)        0                   1
    #           3       1 (AI3)             0                   0.5
    #       And so the expected output would be a list whose length equals
    #           the number of rounds played in each game: [3, 2, 1, 0.5]

    # 4. (bonus) What is the standard distribution of the averages given in
    #    item 1?

    # 5. (bonus) What is the standard distribution of the averages given in
    #    item 3?

    # 6. (bonus) Produce a chart depicting relevant measurements from items
    #    1, and 3, with extra bonus for showing the probability distribution
    #    computed in bonus items 4, and 5


if __name__ == '__main__':
    sim_games()
