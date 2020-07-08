from voting import collect_votes

if __name__ == "__main__":
    votes = collect_votes.get_voters_from_ballots("data/votes.txt")
    print(votes)
