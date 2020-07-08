import pytest

from voting import voter


@pytest.fixture
def turtle_voter():
    return voter.Voter(["turtle", "tiger", "monkey"])


def test_voter_first_choice_is_best_choice(turtle_voter):
    assert turtle_voter.top_choice == "turtle"


def test_convert_to_string(turtle_voter):
    assert str(turtle_voter) == "turtle voter"


def test_repr(turtle_voter):
    assert repr(turtle_voter) == 'Voter(["turtle", "tiger", "monkey"])'


def test_convert_to_csv_line(turtle_voter):
    assert turtle_voter.convert_to_csv_line() == "turtle,tiger,monkey"


def test_elminate_top_choice(turtle_voter):
    turtle_voter.eliminate_top_choice()
    assert turtle_voter.top_choice == "tiger"
    turtle_voter.eliminate_top_choice()
    assert turtle_voter.top_choice == "monkey"


def test_no_vote_after_too_many_elims(turtle_voter):
    for i in range(3):
        turtle_voter.eliminate_top_choice()
    assert turtle_voter.top_choice == None
