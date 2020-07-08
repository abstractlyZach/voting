from pprint import pprint

from voting import collect_votes


if __name__ == "__main__":
    voters = collect_votes.get_voters_from_ranked_choice_vote("data/votes.rcv")
    pprint(voters)
