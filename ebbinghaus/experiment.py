from copy import deepcopy
from time import sleep
from random import randint
from .constant import CONSONANTS, VOWELS, lengthC, lengthV


def start() -> None:

    arg = str(input(
        "To start the program, enter '1'. Otherwise, enter any character to exit. : "))

    if arg != '1':
        print(
            "The program cannot start with any character other than '1'. Please try again.")
        return

    count = int(input("How many CVCs would like to experiment on? : "))

    time = int(input(
        "How many seconds do you want to place in-between display of two CVCs? : "))

    cvcs, answers = create(count=count, time=time)

    print("cvcs : ", cvcs)
    print("answers : ", answers)

    result(cvcs, answers)


def create(cvcs: list[str] = None, count: int = 5, time: int = 1) -> str:

    if count == 0:
        answers = str(
            input("Enter the strings you saw in order separated by a comma (,) : "))
        return [cvcs, list(map(lambda x: x.strip(), answers.split(",")))]

    _cvcs = deepcopy(cvcs)

    c1 = randint(0, lengthC - 1)
    v1 = randint(0, lengthV - 1)
    c2 = randint(0, lengthC - 1)

    cvc = CONSONANTS[c1] + VOWELS[v1] + CONSONANTS[c2]

    if _cvcs is None:
        _cvcs = []
    elif cvc in _cvcs:
        return create(_cvcs, count)
    _cvcs.append(cvc)

    show(_cvcs[-1])
    hide(time)

    return create(_cvcs, count=count - 1)


def show(cvc: str) -> None:
    print(f"\t'{cvc}'", end='\r')


def hide(time: int) -> None:
    sleep(time)


def result(cvcs: list[str], answers: list[str]) -> None:
    logical = []

    for cvc, answer in list(zip(cvcs, answers)):
        if cvc == answer:
            logical.append(True)
        else:
            logical.append(False)

    for index, logic in enumerate(logical):
        if not logic:
            print(
                f"{index + 1} cvc was {cvcs[index]}. But you entered {answers[index]}")

    correctness = len(list(filter(lambda x: x, logical)))
    outof = len(logical)

    proportion: float = round((correctness/outof), 2)

    print(
        f'Total Remembered {correctness}/{outof} - {proportion}')
