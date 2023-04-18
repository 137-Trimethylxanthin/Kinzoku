import datetime
import random
import time
import os
import sys

if sys.argv[1] == 'gui':
    from tkinter import *


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


def answer(num1, num2, op, answer: int):
    if int(eval(f"{num1} {op} {num2}")) == int(answer):
        return True
    else:
        return False


def gui():
    root = Tk()
    root.title("Mathe Spiel")
    lab = Label(root)
    lab.pack()
    root.geometry("500x800")
    root.resizable(False, False)
    root.configure(bg="black")

    clac_flield = Entry(root, width=500, borderwidth=5)
    clac_flield.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    clac_flield.pack()

    # Buttons for calculator
    one = Button(root, text="1", width=10, height=5, bg="white", fg="black")
    one.grid(row=0, column=1)

    two = Button(root, text="2", width=10, height=5, bg="white", fg="black")
    two.grid(row=1, column=1)

    three = Button(root, text="3", width=10, height=5, bg="white", fg="black")
    three.grid(row=2, column=1)

    four = Button(root, text="4", width=10, height=5, bg="white", fg="black")
    four.grid(row=0, column=2)

    five = Button(root, text="5", width=10, height=5, bg="white", fg="black")
    five.grid(row=1, column=2)

    six = Button(root, text="6", width=10, height=5, bg="white", fg="black")
    six.grid(row=2, column=2)

    seven = Button(root, text="7", width=10, height=5, bg="white", fg="black")
    seven.grid(row=0, column=3)

    eight = Button(root, text="8", width=10, height=5, bg="white", fg="black")
    eight.grid(row=1, column=3)

    nine = Button(root, text="9", width=10, height=5, bg="white", fg="black")
    nine.grid(row=2, column=3)

    zero = Button(root, text="0", width=10, height=5, bg="white", fg="black")
    zero.grid(row=3, column=0)

    plus = Button(root, text="+", width=10, height=5, bg="white", fg="black")

    minus = Button(root, text="-", width=10, height=5, bg="white", fg="black")

    mal = Button(root, text="*", width=10, height=5, bg="white", fg="black")

    durch = Button(root, text="/", width=10, height=5, bg="white", fg="black")

    clear = Button(root, text="C", width=10, height=5, bg="white", fg="black")

    enter = Button(root, text="Enter", width=10, height=5, bg="white", fg="black")


    for r in range(3):
        for c in range(4):
            Label(root, text='R%s/C%s' % (r, c), borderwidth=1).grid(row=r, column=c)
    def clock():
        time = datetime.datetime.now().strftime("Time: %H:%M:%S")
        lab.config(text=time)
        root.after(1000, clock)  # run itself again after 1000 ms

    clock()
    root.mainloop()


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
        if answer(num1, num2, op, answer):
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
    if sys.argv[1] == 'gui':
        gui()
    else:
        game_start()
        game()
