#!/usr/bin/env python3
import os
import random
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


"""
a game the language is German

the game is a math game where you have to answer 10 questions
the questions are about multiplication and division and addition and subtraction
the questions are random in the thousand range
under 10 seconds you get 3 points
under 20 seconds you get 2 points
over 20 seconds you get 1 point

if you fail you get 0 points
"""


def game_start():
    clear()
    print("Hallo, willkommen bei dem Mathe Spiel")
    print("Du hast 10 Fragen")
    print("wenn du die Fragen in unter 10 Sekunden beantwortest bekommst du 3 Punkte")
    print("Wenn du die Frage in unter 20 Sekunden beantwortest bekommst du 2 Punkte")
    print("Wenn du die Frage länger als 20 Sekunden beantwortest bekommst du 1 Punkt")
    print("Wenn du die Frage falsch beantwortest bekommst du 0 Punkte")
    print("Wenn du bereit bist drücke Enter")
    input()


def get_division():
    num1: int = random.randint(1, 1000)
    num2: int = random.randint(1, 1000)
    while num1 % num2 != 0 or num1 < num2:
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
    return num1, num2


def get_multiplication():
    num1: int = random.randint(1, 1000)
    num2: int = random.randint(1, 1000)

    while num1 * num2 > 2000:
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)

    return num1, num2


def get_subtraction():
    num1: int = random.randint(1, 1000)
    num2: int = random.randint(1, 1000)

    while num1 < num2:
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)

    return num1, num2


def get_addition():
    num1: int = random.randint(1, 1000)
    num2: int = random.randint(1, 1000)

    while num1 + num2 > 2000:
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)

    return num1, num2


def get_random_question():
    operator: str = random.choice(['+', '-', '*', '/'])
    num1: int = 0
    num2: int = 0
    match operator:
        case '+':
            num1, num2 = get_addition()
        case '-':
            num1, num2 = get_subtraction()
        case '*':
            num1, num2 = get_multiplication()
        case '/':
            num1, num2 = get_division()

    return num1, num2, operator


def custom_input(question: str):
    while True:
        try:
            print(question, end="")
            answer = int(input())
        except ValueError:
            print("Bitte eine Zahl eingeben")
            continue
        else:
            return answer


def test_answer(num1, num2, op, answer: int):
    if int(eval(f"{num1} {op} {num2}")) == int(answer):
        return True
    else:
        return False


def end_game(punkte: int):
    term_x: int = os.get_terminal_size().columns
    term_y: int = os.get_terminal_size().lines

    clear()
    print("Das Spiel ist zu Ende".center(term_x, "-"))
    for i in range(term_y // 2 - 2):
        print()

    if punkte == 1:
        print(f"Du hast {punkte} Punkt".center(term_x))
    else:
        print(f"Du hast {punkte} Punkte erreicht".center(term_x))

    if punkte == 30:
        print("Du hast alle Fragen unter 10 sekunden beantwortet".center(term_x))
    elif punkte >= 20:
        print("Du hast die meisten Fragen richtig beantwortet".center(term_x))
    elif punkte >= 10:
        print("Du hast die Hälfte der Fragen richtig beantwortet".center(term_x))
    elif punkte == 0:
        print("Du hast alle Fragen falsch beantwortet".center(term_x))
    else:
        print("Du hast die meisten Fragen falsch beantwortet".center(term_x))

    for i in range(term_y // 2 - 2):
        print()


def game_cli():
    game_start()
    questions: int = 10
    points: int = 0
    clear()
    while questions > 0:
        num1, num2, op = get_random_question()
        start = time.time()
        answer: int = custom_input(f"{num1} {op} {num2} = ")
        end = time.time()
        questions -= 1
        timer: float = end - start
        if test_answer(num1, num2, op, answer):
            print("Richtig")
            if timer <= 10:
                points += 3
            elif timer <= 20:
                points += 2
            else:
                points += 1
        else:
            print("Falsch")
            print(f"Die richtige Antwort ist {int(eval(f'{num1} {op} {num2}'))}")

        print(f"Du hast {timer.__round__(2)} Sekunden gebraucht")
        if questions == 1:
            print(f"Du hast noch {questions} Frage, lets go")
            print(f"-------------------Nächste Frage-------------------")
        elif questions == 0:
            pass
        else:
            print(f"Du hast noch {questions} Fragen")
            print(f"-------------------Nächste Frage-------------------")

    end_game(points)


if __name__ == '__main__':
    game_cli()
