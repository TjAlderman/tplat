import pytest
from poker.main import Player, distribute_winnings

def test_poker():
    print("Testing the player classes...")

    james_c = Player(name='James C.',expenses=20,winnings=24)
    james_o = Player(name='James O.',expenses=20,winnings=16)
    angus = Player(name='Angus',expenses=20,winnings=0)
    ted = Player(name='Ted',expenses=20,winnings=40)
    players = [james_c,james_o,angus,ted]
    assert (players[0].name=="James C.") and (players[1].expenses==20) and (players[2].winnings==0)

    print("Testing the distribute winnings function...")
    distribute_winnings(players=players)

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-s"]))