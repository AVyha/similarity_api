import dataclasses
from copy import copy

from pydantic import BaseModel


@dataclasses.dataclass
class Model:
    name: str
    cnt: int
    info: str


class ModelSchema(BaseModel):
    name: str
    info: str = ""


def get_all_names(ls: list[Model]) -> list:
    ls.sort(key=lambda x: x.cnt, reverse=True)
    names = []

    for elem in ls:
        names.append(elem.name)

    return names


def similarity_percent(first_word, second_word):
    diff = abs(len(first_word) - len(second_word))

    for first_char, second_char in zip(first_word, second_word):
        if first_char != second_char:
            diff += 1

    return 100 - (100 / max(len(first_word), len(second_word)) * diff)


def most_similarity(ls: list[Model], word: str) -> list:
    ls.sort(key=lambda x: similarity_percent(word, x.name), reverse=True)
    return ls


def add_count(name: str, ls: list[Model]):
    ls = copy(ls)
    ls = most_similarity(ls, name)

    equal_similarity = []

    try:
        num = similarity_percent(name, ls[0].name)

        while similarity_percent(name, ls[0].name) == num:
            equal_similarity.append(ls.pop(0))
    except IndexError:
        pass

    for char in equal_similarity:
        char.cnt += 1

    return equal_similarity


