import csv
import typing

from . import voter


EMPTY_VOTE = ""
DELIMITER = ","


def get_voters_from_ballots(path: str) -> typing.List[voter.Voter]:
    voters = []
    with open(path, "r") as infile:
        reader = csv.DictReader(infile)
        for vote in reader:
            ranked_choices = convert_ballot_to_ranked_choice(vote)
            voters.append(voter.Voter(ranked_choices))
    return voters


def convert_ballot_to_ranked_choice(ballot: typing.Dict) -> typing.List:
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
    voters = []
    with open(path, "r") as infile:
        for line in infile:
            ranked_choices = line.strip().split(DELIMITER)
            voters.append(voter.Voter(ranked_choices))
    return voters
