import collections
import typing


class Election(object):
    """
    An Election is a group of Voters and can perform actions and analysis to find a winner.
    """

    def __init__(self, voters) -> None:
        self._voters = voters
        self._vote_counter = collections.Counter(
            voter.top_choice for voter in self._voters
        )


class FirstPastThePostElection(Election):
    """
    Voters get one choice and the candidate that has the most votes wins!
    """

    def count_votes(self) -> collections.Counter:
        return self._vote_counter

    def get_percentages(self) -> typing.Dict:
        vote_percentages = collections.OrderedDict()
        for candidate, num_votes in self._vote_counter.most_common():
            vote_percentages[candidate] = (num_votes / len(self._voters)) * 100
        return vote_percentages

    def most_common(self, n=None):
        return self._vote_counter.most_common(n=n)

    def __str__(self) -> str:
        string = f"Winner: {self.most_common(1)[0][0]}"
        string += "\n\n"
        string += "Results:\n"
        for candidate, percentage in self.get_percentages().items():
            string += f"\t{candidate:10}: {percentage:04}%\n"
        return string
