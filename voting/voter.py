import typing


class Voter:
    def __init__(self, choices: typing.List[str]):
        if len(choices) <= 0:
            raise Exception(f"No choices listed when creating a voter")
        self._choices = choices
        self._best_choice_index = 0

    @property
    def top_choice(self) -> typing.Optional[str]:
        try:
            return self._choices[self._best_choice_index]
        except IndexError:
            return None

    def eliminate_top_choice(self) -> None:
        self._best_choice_index += 1

    def __str__(self):
        return f"{self._choices[0]} voter"

    def __repr__(self):
        return str(self)
