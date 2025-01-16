from planet.blackjack.models import Shoe
from planet.blackjack.blackjack import Blackjack, blackjack_main
import pytest


class FakeShoe(Shoe):
    def shuffle(self):
        # Fake shuffle that preserves card order
        self._undealt_cards = len(self._cards)


@pytest.fixture
def deterministic_game():
    game = Blackjack(shoe=FakeShoe())
    return game


def test_blackjack_main(deterministic_game):
    blackjack_main(
        ai=["ai1", "ai2", "ai3"], num_rounds=3, game=deterministic_game)
    assert deterministic_game.round == 4
    players = deterministic_game.betters
    assert players['ai1'].money == 1125
    assert players['ai2'].money == 1125
    assert players['ai3'].money == 1875
