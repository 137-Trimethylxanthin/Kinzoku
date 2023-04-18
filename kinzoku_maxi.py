import random
import time
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


"""
a game the language is German

the game is a math game where you have to awnser 10 questions
the questions are about multiplication and division and addition and subtraction
the questions are random in the thousend range
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


def get_random_question():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    operator = random.choice(['+', '-', '*', '/'])
    if operator == '/':
        while num1 % num2 != 0:
            num1 = random.randint(1, 1000)
            num2 = random.randint(1, 1000)
    return num1, num2, operator


def custom_input():
    while True:
        try:
            answer = int(input())
        except ValueError:
            print("Bitte eine Zahl eingeben")
            continue
        else:
            return answer


def awnser(num1, num2, op, answer: int):
    if int(eval(f"{num1} {op} {num2}")) == int(answer):
        return True
    else:
        return False


def game():
    questions: int = 10
    points: int = 0
    timer: float = 0
    clear()
    while questions > 0:
        num1, num2, op = get_random_question()
        print(f"{num1} {op} {num2} = ", end="")
        start = time.time()
        answer = custom_input()
        end = time.time()
        questions -= 1
        timer = end - start
        if awnser(num1, num2, op, answer):
            print("Richtig")
            if timer < 10:
                points += 3
            elif timer < 20:
                points += 2
            else:
                points += 1
        else:
            print("Falsch")
            print(f"Die richtige Antwort ist {int(eval(f'{num1} {op} {num2}'))}")

        print(f"Du hast {timer.__round__(2)} Sekunden gebraucht")
        if questions == 1:
            print(f"Du hast noch {questions} Frage, lets go")
            print(f"-------------------nexte Frage-------------------")
        elif questions == 0:
            pass
        else:
            print(f"Du hast noch {questions} Fragen")
            print(f"-------------------nexte Frage-------------------")

    print("--------------------Das Spiel ist vorbei-------------------")
    print(f"Du hast {points} Punkte erreicht")


if __name__ == '__main__':
    game_start()
    game()
