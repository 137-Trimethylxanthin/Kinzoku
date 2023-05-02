#!/usr/bin/env python3
version: str = "1.0.0"
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
    print("Hallo, willkommen bei dem Mathespiel.")
    print("Du bekommst 10 Fragen zum Antworten.")
    print("Wenn du die Frage in unter 10 Sekunden beantwortest, bekommst du 3 Punkte.")
    print("Wenn du die Frage in unter 20 Sekunden beantwortest, bekommst du 2 Punkte.")
    print("Wenn du für die Beantwortung länger als 20 Sekunden brauchst, bekommst du 1 Punkt.")
    print("Wenn du die Frage falsch beantwortest, bekommst du 0 Punkte.")
    print("Drücke die Enter-Taste zum Starten.")
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


class Gui(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.fame = None
        self.sad: int = 1000
        self.geometry("800x950")
        self.resizable(False, False)
        self.title("Mathe Spiel")
        self.configure(bg="#24273a")
        self.punkte: int = 0
        self.counter: int = 0

        self.switch(StartFrame)

    def switch(self, cframe):
        if self.fame != None:
            self.fame.destroy()
        self.fame = cframe(self)
        self.fame.pack()


class StartFrame(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.window = window
        print(self.window.sad)

        self.configure(bg="#24273a")

        self.lable = tk.Label(self, text="Hallo, willkommen zu unseren Mathe Spiel", font=("Arial", 20), pady=20,
                              bg="#24273a", fg="#cad3f5")
        self.lable.pack()

        self.lable = tk.Label(self,
                              text="Du hast 10 Fragen\nWenn du eine frage unter 10 sekunden beantwortest bekommst du 3 "
                                   "punkte\n unter 20 sekunden 2 punkte\nUnd alles länger als 20 sekunden 1 "
                                   "punkt\nfalsch beantwortete frage bekommen 0 punkte",
                              font=("Arial", 16), pady=100, bg="#24273a", fg="#cad3f5", )
        self.lable.pack()

        self.button = tk.Button(self, text="Start", font=("Arial", 40, "bold"),
                                command=lambda: self.window.switch(GameFrame), pady=20,
                                width=10,
                                height=1, bg="#a6da95", fg="#181926", borderwidth=0, activebackground="#8bd5ca",
                                activeforeground="#181926", cursor="hand2")
        self.button.pack()

    def egal(self):
        print(self.window.sad)


class GameFrame(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.window = window
        self.start_time: float = time.time()
        self.now_numbers: str = ""
        self.question: str = ""
        self.done: bool = False
        self.num1: int = 0
        self.num2: int = 0
        self.op: str = ""
        self.window.geometry("800x650")
        self.calc = tk.Frame(width=500, height=650, bg="#24273a")
        self.calc.pack_propagate(False)

        def new_question():
            self.num1, self.num2, self.op = get_random_question()
            self.question = f"{self.num1} {self.op} {self.num2} = "

        new_question()

        def button_click(number):
            if number != "del" and number != "enter" and not self.done:
                self.now_numbers += str(number)
                self.text.delete(1.0, "end")
                self.text.insert(1.0, self.question + self.now_numbers)
            elif number == "del" and not self.done:
                self.now_numbers = self.now_numbers[:-1]
                self.text.delete(1.0, "end")
                self.text.insert(1.0, self.question + self.now_numbers)
            elif number == "enter" and not self.done and self.now_numbers != "":
                if test_answer(self.num1, self.num2, self.op, int(self.now_numbers)):
                    self.text.delete(1.0, "End")
                    self.text.insert(1.0, "Richtig")
                    self.text.insert(2.0, f"\nZeit: {(time.time() - self.start_time).__round__(2)} s")
                    if (time.time() - self.start_time) < 10:
                        self.window.punkte += 3
                    elif (time.time() - self.start_time) < 20:
                        self.window.punkte += 2
                    else:
                        self.window.punkte += 1
                else:
                    self.text.delete(1.0, "End")
                    self.text.insert(1.0, "Falsch")
                    self.text.insert(2.0,
                                     f"\nrichtig: {self.question}{int(eval(f'{self.num1} {self.op} {self.num2}'))}")
                self.done = True
            elif number == "enter" and self.done:
                self.now_numbers = ""
                self.window.counter += 1
                self.counterlable.configure(text=f"")
                new_question()
                self.text.delete(1.0, "End")
                self.text.insert(1.0, self.question + self.now_numbers)
                self.start_time = time.time()
                self.done = False
                if self.window.counter == 9:
                    self.calc.destroy()
                    self.window.switch(EndFrame)


        #infos

        self.counterlable = tk.Label(self, text=f"Frage: {self.window.counter}",font=("Arial", 32), width=20, height=2, bg="#181926", fg="#cad3f5")



        #calculator

        self.calc.columnconfigure(0, weight=1)
        self.calc.columnconfigure(1, weight=1)
        self.calc.columnconfigure(2, weight=1)
        self.calc.columnconfigure(3, weight=1)

        self.text = tk.Text(self.calc, font=("Arial", 32), width=20, height=2, bg="#181926", fg="#cad3f5", borderwidth=0,
                            highlightthickness=5, insertbackground="#cad3f5", highlightbackground="#494d64", )
        self.text.grid(columnspan=3, pady=20)
        self.question = f"{self.num1} {self.op} {self.num2} = "
        self.text.delete(1.0, "end")
        self.text.insert(1.0, self.question)

        self.btn7 = tk.Button(self.calc, text="7", font=("Arial", 30), height=2, command=lambda: button_click(7))
        self.btn7.grid(row=1, column=0, sticky="nsew", pady=2, padx=4)

        self.btn8 = tk.Button(self.calc, text="8", font=("Arial", 30), height=2, command=lambda: button_click(8))
        self.btn8.grid(row=1, column=1, sticky="nsew", pady=2, padx=4)

        self.btn9 = tk.Button(self.calc, text="9", font=("Arial", 30), height=2, command=lambda: button_click(9))
        self.btn9.grid(row=1, column=2, sticky="nsew", pady=2, padx=4)

        self.btn4 = tk.Button(self.calc, text="4", font=("Arial", 30), height=2, command=lambda: button_click(4))
        self.btn4.grid(row=2, column=0, sticky="nsew", pady=2, padx=4)

        self.btn5 = tk.Button(self.calc, text="5", font=("Arial", 30), height=2, command=lambda: button_click(5))
        self.btn5.grid(row=2, column=1, sticky="nsew", pady=2, padx=4)

        self.btn6 = tk.Button(self.calc, text="6", font=("Arial", 30), height=2, command=lambda: button_click(6))
        self.btn6.grid(row=2, column=2, sticky="nsew", pady=2, padx=4)

        self.btn1 = tk.Button(self.calc, text="1", font=("Arial", 30), height=2, command=lambda: button_click(1))
        self.btn1.grid(row=3, column=0, sticky="nsew", pady=2, padx=4)

        self.btn2 = tk.Button(self.calc, text="2", font=("Arial", 30), height=2, command=lambda: button_click(2))
        self.btn2.grid(row=3, column=1, sticky="nsew", pady=2, padx=4)

        self.btn3 = tk.Button(self.calc, text="3", font=("Arial", 30), height=2, command=lambda: button_click(3))
        self.btn3.grid(row=3, column=2, sticky="nsew", pady=2, padx=4)

        self.btn0 = tk.Button(self.calc, text="0", font=("Arial", 30), height=2, command=lambda: button_click(0))
        self.btn0.grid(row=4, column=1, sticky="nsew", pady=2, padx=4)

        self.btn_del = tk.Button(self.calc, text="C", font=("Arial", 30), height=2, command=lambda: button_click("del"))
        self.btn_del.grid(row=4, column=0, sticky="nsew", pady=2, padx=4)

        self.btn_enter = tk.Button(self.calc, text="=", font=("Arial", 30), height=2, command=lambda: button_click("enter"))
        self.btn_enter.grid(row=4, column=2, sticky="nsew", pady=2, padx=4)

        self.calc.pack()

class EndFrame(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.window = window

        def restart():
            self.window.punkte = 0
            self.window.counter = 0
            self.window.switch(GameFrame)

        self.lable = tk.Label(self, text=f"Ende\nDu hast {self.window.punkte} punkte erhalten", font=("Arial", 30), bg="#24273a", fg="#cad3f5")
        self.lable.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=2, padx=4)

        self.button = tk.Button(self, text="Neues Spiel", font=("Arial", 30), height=2, command=lambda: restart(), bg="#24273a", fg="#cad3f5")
        self.button.grid(row=2, column=0, columnspan=2, sticky="nsew", pady=2, padx=8)

        self.button = tk.Button(self, text="Beenden", font=("Arial", 30), height=2, command=lambda: self.window.destroy(), bg="#24273a", fg="#cad3f5")
        self.button.grid(row=2, column=2, columnspan=2, sticky="nsew", pady=2, padx=8)


if __name__ == '__main__':
    argparse = argparse.ArgumentParser()
    argparse.add_argument("-g", "--gui", help="Startet das Spiel mit GUI", action="store_true", dest="gui")
    argparse.add_argument("-c", "--cli", help="Startet das Spiel in der Konsole", action="store_true")
    argparse.add_argument("-v", "--version", help="Zeigt die Version an", action="store_true")
    args = argparse.parse_args()
    if args.gui:
        print("hi")
        app = Gui()
        app.mainloop()
    elif args.cli:
        game_cli()
    elif args.version:
        print(f"Version: {version}")
    else:
        print("Bitte gib eine Option an")
        print("Benutze -h oder --help für Hilfe")
        print("oder starte das spiel mit -g oder -c")
        print("siehe help für mehr informationen")
