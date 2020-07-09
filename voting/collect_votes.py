import csv
import typing

from . import voter


EMPTY_VOTE = ""
DELIMITER = ","


def get_voters_from_ballots(path: str) -> typing.List[voter.Voter]:
    """
    Convert a path to a ballot file into voters.

    A ballot file is a CSV with candidates listed in the header and each line below
    that represents a voter's submission, with "1" marking their first choice, "2"
    marking their second choice, etc.
    ex.
    ```
    tiger,lion,bear
    1,,
    ,1,
    1,2,
    2,,1
    ```
    """
    voters = []
    with open(path, "r") as infile:
        reader = csv.DictReader(infile)
        for vote in reader:
            ranked_choices = convert_ballot_to_ranked_choice(vote)
            voters.append(voter.Voter(ranked_choices))
    return voters


def convert_ballot_to_ranked_choice(ballot: typing.Dict) -> typing.List:
    """Convert a ballot into a ranked choice list."""
    rank_to_candidate = {
        int(rank): candidate for candidate, rank in ballot.items() if rank != EMPTY_VOTE
    }
    ranked_candidates = []
    for i in range(1, 10):
        if i in rank_to_candidate:
            ranked_candidates.append(rank_to_candidate[i])
        else:
            break
    return ranked_candidates


def get_voters_from_ranked_choice_vote(path: str) -> typing.List[voter.Voter]:
    """
    Read a ranked-choice vote file and convert it into a list of Voter objects.

    A ranked-choice vote file is a CSV file with no header where each line represents
    a voter's submission, in order from first choice to last choice left-to-right
    """
    voters = []
    with open(path, "r") as infile:
        for line in infile:
            ranked_choices = line.strip().split(DELIMITER)
            voters.append(voter.Voter(ranked_choices))
    return voters
