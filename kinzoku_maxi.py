#!/usr/bin/env python3
import argparse
import os
import random
import time
import tkinter as tk


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


def game_gui():
    counter: int = 0
    start_time: float = 0
    now_numbers = ""
    question = ""
    done: bool = False
    punkte: int = 0

    root = tk.Tk()
    root.geometry("1000x500")
    root.resizable(False, False)
    root.title("Mathe Spiel")
    root.configure(bg="#24273a")

    startFrame = tk.Frame(root, bg="#24273a")
    gameFrame = tk.Frame(root, bg="#24273a")
    endFrame = tk.Frame(root, bg="#24273a")

    lable = tk.Label(startFrame, text="Hallo, willkommen zu unseren Mathe Spiel", font=("Arial", 20), pady=20,
                     bg="#24273a", fg="#cad3f5")
    lable.pack()

    lable = tk.Label(startFrame,
                     text="Du hast 10 Fragen\nWenn du eine frage unter 10 sekunden beantwortest bekommst du 3 "
                          "punkte\n unter 20 sekunden 2 punkte\nUnd alles länger als 20 sekunden 1 "
                          "punkt\nfalsch beantwortete frage bekommen 0 punkte",
                     font=("Arial", 16), pady=100, bg="#24273a", fg="#cad3f5", )
    lable.pack()

    def game_gui_start():
        nonlocal start_time
        startFrame.pack_forget()
        root.geometry("500x550")
        root.resizable(False, False)
        root.title("Mathe Spiel - Spielen")
        root.configure(bg="#24273a")
        gameFrame.pack(fill="both", expand=True)
        start_time = time.time()

    button = tk.Button(startFrame, text="Start", font=("Arial", 40, "bold"), command=game_gui_start, pady=20, width=10,
                       height=1, bg="#a6da95", fg="#181926", borderwidth=0, activebackground="#8bd5ca",
                       activeforeground="#181926", cursor="hand2")
    button.pack()
    startFrame.pack(expand=True)

    # start of game frame
    num1, num2, op = get_random_question()

    def new_question():
        nonlocal num1, num2, op, question
        num1, num2, op = get_random_question()
        question = f"{num1} {op} {num2} = "

    def game_gui_end():
        nonlocal punkte
        temp: str = "Punkte"
        gameFrame.pack_forget()
        root.geometry("500x550")
        root.resizable(False, False)
        root.title("Mathe Spiel - Ende")
        root.configure(bg="#24273a")
        if punkte == 1:
            temp = "Punkt"
        lable = tk.Label(endFrame, text=f"Das Spiel ist zu Ende\nDabei hast du {punkte} punkte erreicht.",
                         font=("Arial", 20), pady=20, bg="#24273a", fg="#cad3f5")
        lable.grid(row=0, columnspan=4, sticky="nsew")

        endFrame.pack(fill="both", expand=True)

    def button_click(number):
        nonlocal now_numbers, question, done, start_time, counter, punkte
        if number != "del" and number != "enter" and not done:
            now_numbers += str(number)
            text.delete(1.0, "end")
            text.insert(1.0, question + now_numbers)
        elif number == "del" and not done:
            now_numbers = now_numbers[:-1]
            text.delete(1.0, "end")
            text.insert(1.0, question + now_numbers)
        elif number == "enter" and not done and now_numbers != "":
            if test_answer(num1, num2, op, int(now_numbers)):
                text.delete(1.0, "end")
                text.insert(1.0, "richtig")
                text.insert(2.0, f"\nzeit: {(time.time() - start_time).__round__(2)} s")
                if (time.time() - start_time) < 10:
                    punkte += 3
                elif (time.time() - start_time) < 20:
                    punkte += 2
                else:
                    punkte += 1

            else:
                text.delete(1.0, "end")
                text.insert(1.0, "falsch")
                text.insert(2.0, f"\nrichtig: {question}{int(eval(f'{num1} {op} {num2}'))}")
            done = True
        elif number == "enter" and done:
            now_numbers = ""
            if counter == 9:
                game_gui_end()
            counter += 1
            new_question()
            text.delete(1.0, "end")
            text.insert(1.0, question + now_numbers)
            start_time = time.time()
            done = False

    gameFrame = tk.Frame(root)
    gameFrame.columnconfigure(0, weight=1)
    gameFrame.columnconfigure(1, weight=1)
    gameFrame.columnconfigure(2, weight=1)
    gameFrame.columnconfigure(3, weight=1)
    gameFrame.configure(bg="#24273a")

    text = tk.Text(gameFrame, font=("Arial", 32), width=45, height=2, bg="#181926", fg="#cad3f5", borderwidth=0,
                   highlightthickness=5, insertbackground="#cad3f5", highlightbackground="#494d64", )
    text.grid(columnspan=3, pady=20)
    question = f"{num1} {op} {num2} = "
    text.delete(1.0, "end")
    text.insert(1.0, question)

    btn7 = tk.Button(gameFrame, text="7", font=("Arial", 30), height=2, command=lambda: button_click(7))
    btn7.grid(row=1, column=0, sticky="nsew", pady=2, padx=4)

    btn8 = tk.Button(gameFrame, text="8", font=("Arial", 30), height=2, command=lambda: button_click(8))
    btn8.grid(row=1, column=1, sticky="nsew", pady=2, padx=4)

    btn9 = tk.Button(gameFrame, text="9", font=("Arial", 30), height=2, command=lambda: button_click(9))
    btn9.grid(row=1, column=2, sticky="nsew", pady=2, padx=4)

    btn4 = tk.Button(gameFrame, text="4", font=("Arial", 30), height=2, command=lambda: button_click(4))
    btn4.grid(row=2, column=0, sticky="nsew", pady=2, padx=4)

    btn5 = tk.Button(gameFrame, text="5", font=("Arial", 30), height=2, command=lambda: button_click(5))
    btn5.grid(row=2, column=1, sticky="nsew", pady=2, padx=4)

    btn6 = tk.Button(gameFrame, text="6", font=("Arial", 30), height=2, command=lambda: button_click(6))
    btn6.grid(row=2, column=2, sticky="nsew", pady=2, padx=4)

    btn1 = tk.Button(gameFrame, text="1", font=("Arial", 30), height=2, command=lambda: button_click(1))
    btn1.grid(row=3, column=0, sticky="nsew", pady=2, padx=4)

    btn2 = tk.Button(gameFrame, text="2", font=("Arial", 30), height=2, command=lambda: button_click(2))
    btn2.grid(row=3, column=1, sticky="nsew", pady=2, padx=4)

    btn3 = tk.Button(gameFrame, text="3", font=("Arial", 30), height=2, command=lambda: button_click(3))
    btn3.grid(row=3, column=2, sticky="nsew", pady=2, padx=4)

    btn0 = tk.Button(gameFrame, text="0", font=("Arial", 30), height=2, command=lambda: button_click(0))
    btn0.grid(row=4, column=1, sticky="nsew", pady=2, padx=4)

    btn_del = tk.Button(gameFrame, text="C", font=("Arial", 30), height=2, command=lambda: button_click("del"))
    btn_del.grid(row=4, column=0, sticky="nsew", pady=2, padx=4)

    btn_enter = tk.Button(gameFrame, text="=", font=("Arial", 30), height=2, command=lambda: button_click("enter"))
    btn_enter.grid(row=4, column=2, sticky="nsew", pady=2, padx=4)

    # End Frame

    def restart():
        nonlocal counter, punkte
        counter = 0
        punkte = 0

        endFrame.pack_forget()
        #new_question()
        #text.delete(1.0, "end")
        #text.insert(1.0, question + now_numbers)
        game_gui_start()

    button = tk.Button(endFrame, text="Neues Spiel", font=("Arial", 30), height=2, command=lambda: restart())
    button.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=2, padx=4)

    button = tk.Button(endFrame, text="Beenden", font=("Arial", 30), height=2, command=lambda: root.destroy())
    button.grid(row=1, column=2, columnspan=2, sticky="nsew", pady=2, padx=4)

    root.mainloop()


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
    game_gui()
