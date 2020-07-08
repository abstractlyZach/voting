from pprint import pprint

from voting import collect_votes


if __name__ == "__main__":
    voters = collect_votes.get_voters_from_ballots("data/votes.txt")
    with open("data/votes.rcv", "w") as outfile:
        for voter in voters:
            outfile.write(voter.convert_to_csv_line() + "\n")
