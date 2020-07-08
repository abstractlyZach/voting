import typing


class Voter:
    def __init__(self, choices: typing.List[str]) -> None:
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

    def __str__(self) -> str:
        return f"{self._choices[0]} voter"

    def __repr__(self) -> str:
        quote_wrapped_choices = [f'"{choice}"' for choice in self._choices]
        list_inner_string = ", ".join(quote_wrapped_choices)
        return f"Voter([{list_inner_string}])"

    def convert_to_csv_line(self) -> str:
        return ",".join(self._choices)
