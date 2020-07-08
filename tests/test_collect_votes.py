from voting import collect_votes


def test_convert_ballot_ranked_choice_one_vote():
    ballot = {"turtle": "1", "potato": "", "monkey": "", "hippo": ""}
    expected = ["turtle"]
    actual = collect_votes.convert_ballot_to_ranked_choice(ballot)
    assert actual == expected


def test_convert_ballot_ranked_choice_multiple():
    ballot = {"turtle": "", "potato": "2", "monkey": "1", "hippo": ""}
    expected = ["monkey", "potato"]
    actual = collect_votes.convert_ballot_to_ranked_choice(ballot)
    assert actual == expected
