#!/usr/bin/env python3
version: str = "1.1.0"
import argparse
import os
import random
import time
import tkinter as tk

theme: dict = {
    "Base": "#24273a",
    "Mantle": "#1e2030",
    "Crust": "#181926",
    "Surface0": "#363a4f",
    "Surface1": "#494d64",
    "Surface2": "#5b6078",
    "Overlay0": "#6e738d",
    "Overlay1": "#8087a2",
    "Overlay2": "#939ab7",
    "Subtext0": "#a5adcb",
    "Subtext1": "#b8c0e0",
    "Text": "#cad3f5",
    "AccentG": "#a6da95",
    "AccentM": "#c6a0f6",
    "AccentPi": "#f5bde6",
    "AccentPe": "#f5a97f",
    "AccentB": "#8aadf4",
}


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
    difficulty: int = None
    while difficulty not in [0, 1, 2]:
        clear()
        print("Hallo, willkommen bei dem Mathespiel.")
        print("Du bekommst 10 Fragen zum Antworten.")
        print("Wenn du die Frage in unter 10 Sekunden beantwortest, bekommst du 3 Punkte.")
        print("Wenn du die Frage in unter 20 Sekunden beantwortest, bekommst du 2 Punkte.")
        print("Wenn du für die Beantwortung länger als 20 Sekunden brauchst, bekommst du 1 Punkt.")
        print("Wenn du die Frage falsch beantwortest, bekommst du 0 Punkte.")
        print("EasyMode: Du bekommst 2-6 antworten zur Auswahl, wähle die richtige aus.")
        print("NormalMode: Du musst die Antwort selber eingeben. aber kein ergebniss geht über 2000 und ist immer "
              "ganzstellig")
        print("HardMode: Du musst die Antwort selber eingeben. ES WIRD IMMER ABGERUNDET")
        print("Wähle den Schwierigkeitsgrad")
        print("0: EasyMode")
        print("1: NormalMode")
        print("2: HardMode")
        difficulty = custom_input("Schwierigkeitsgrad: ")
    clear()
    return difficulty


def get_division(dificulty: int = 1):
    num1: int = random.randint(1, 1000)
    num2: int = random.randint(1, 1000)
    if dificulty == 2:
        while num1 < num2:
            num1 = random.randint(1, 10000)
            num2 = random.randint(1, 10000)
    else:
        while num1 % num2 != 0 or num1 < num2:
            num1 = random.randint(1, 1000)
            num2 = random.randint(1, 1000)
    return num1, num2


def get_multiplication(dificulty: int = 1):
    num1: int = random.randint(1, 1000)
    num2: int = random.randint(1, 1000)
    while num1 * num2 > 2000 and not dificulty == 2:
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


def get_addition(dificulty: int = 1):
    num1: int = random.randint(1, 1000)
    num2: int = random.randint(1, 1000)

    while num1 + num2 > 2000 and not dificulty == 2:
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)

    return num1, num2


def get_random_question(dificulty: int = 1):
    operator: str = random.choice(['+', '-', '*', '/'])
    num1: int = 0
    num2: int = 0
    match operator:
        case '+':
            num1, num2 = get_addition(dificulty)
        case '-':
            num1, num2 = get_subtraction()
        case '*':
            num1, num2 = get_multiplication(dificulty)
        case '/':
            num1, num2 = get_division(dificulty)

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


def end_game(punkte: int, d: int):
    term_x: int = os.get_terminal_size().columns
    term_y: int = os.get_terminal_size().lines

    if d == 0:
        difficulty = "Easy"
    elif d == 1:
        difficulty = "Normal"
    elif d == 2:
        difficulty = "Hard"

    clear()
    print("Das Spiel ist zu Ende".center(term_x, "-"))
    for i in range(term_y // 2 - 2):
        print()

    if punkte == 1:
        print(f"Du hast {punkte} Punkt".center(term_x))
    else:
        print(f"Du hast {punkte} Punkte erreicht".center(term_x))

    print(f"du hast auf der Schwierigkeit {difficulty} gespielt".center(term_x))

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


def fake_answer(answer: int):
    if answer <= 100:
        return random.randint(0, 100)
    else:
        return random.randint(answer - 100, answer + 100)


def game_cli():
    difficulty: int = game_start()
    answers_list: list[int] = []
    questions: int = 10
    points: int = 0
    ammount: int = 1
    choice: int = 0
    clear()
    while questions > 0:
        num1, num2, op = get_random_question(difficulty)
        if difficulty == 0:
            answers_list.append(int(eval(f"{num1} {op} {num2}")))
            for i in range(ammount):
                answers_list.append(fake_answer(int(eval(f"{num1} {op} {num2}"))))
            random.shuffle(answers_list)
            start = time.time()
            while choice < 1 or choice > len(answers_list):
                clear()
                print(f"{num1} {op} {num2} = ")
                for i in range(len(answers_list)):
                    print(f"{i + 1}: {answers_list[i]}")
                choice: int = custom_input("Antwort: ")
            answer = int(answers_list[choice - 1])
            print(answers_list, answer)
            answers_list.clear()
            choice = 0
        else:
            start = time.time()
            answer: int = custom_input(f"{num1} {op} {num2} = ")
        end = time.time()
        questions -= 1
        timer: float = end - start
        clear()
        print(f"{num1} {op} {num2} = {answer}")
        if test_answer(num1, num2, op, answer):
            print("Richtig")
            if timer <= 10:
                points += 3
            elif timer <= 20:
                points += 2
            else:
                points += 1

            if ammount <= 6:
                ammount += 1
        else:
            print("Falsch")
            print(f"Die richtige Antwort ist {int(eval(f'{num1} {op} {num2}'))}")
            if ammount > 1:
                ammount -= 1

        print(f"Du hast {timer.__round__(2)} Sekunden gebraucht")
        if questions == 1:
            print(f"Du hast noch {questions} Frage, lets go")
            print(f"-------------------Nächste Frage-------------------")
        elif questions == 0:
            pass
        else:
            print(f"Du hast noch {questions} Fragen")
            print(f"-------------------Nächste Frage-------------------")

    end_game(points, difficulty)


class Gui(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.fame = None
        self.sad: int = 1000
        self.geometry("1100x700")
        self.resizable(False, False)
        self.title("Mathe Spiel")
        self.configure(bg=theme["Base"])
        self.punkte: int = 0
        self.counter: int = 1
        self.rounds: int = 10
        self.mode = tk.IntVar()
        self.choise = tk.IntVar()
        self.startOfGame: float = 0

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
        self.window.mode.set(1)

        self.configure(bg="#24273a")

        self.lable = tk.Label(self, text="Hallo, willkommen zu unseren Mathe Spiel", font=("Arial", 30, "bold"),
                              pady=20,
                              bg="#24273a", fg="#cad3f5")
        self.lable.pack()

        self.lable = tk.Label(self,
                              text="Du hast 10 Fragen\nWenn du eine frage unter 10 sekunden beantwortest bekommst du 3 "
                                   "punkte\n unter 20 sekunden 2 punkte\nUnd alles länger als 20 sekunden 1 "
                                   "punkt\nfalsch beantwortete frage bekommen 0 punkte\n\nDer Normal mode hat limits: "
                                   "ergebnisse nicht über 2000 und nur ganzzahlige divisionen\nDer Hard mode hat keine limits"
                                   " wie hoch die ergebnisse sein können und Divisionen werden AB-GERUNDET\nEasy mode hat"
                                   " die gleichen limits wie Normal mode aber hat 2-6 auswahlmöglichkeiten die ausgewehlt"
                                   " werden können\nViel Spaß",
                              font=("Arial", 16), pady=20, bg="#24273a", fg="#cad3f5", )
        self.lable.pack()

        self.button = tk.Button(self, text="Start", font=("Arial", 40, "bold"),
                                command=lambda: self.window.switch(GameFrame), pady=20,
                                width=10,
                                height=1, bg="#a6da95", fg="#181926", borderwidth=0, activebackground="#8bd5ca",
                                activeforeground="#181926", cursor="hand2")
        self.button.pack(pady=20)

        self.easyMode = tk.Radiobutton(self, text="Easy Mode", font=("Arial", 30, "bold"), variable=self.window.mode,
                                       value=0, bg="#24273a",
                                       fg="#cad3f5", selectcolor="#24273a", activebackground="#24273a",
                                       activeforeground=theme["Overlay0"], cursor="hand2")
        self.easyMode.pack(side="left", padx=50, )

        self.normalMode = tk.Radiobutton(self, text="Normal Mode", font=("Arial", 30, "bold"),
                                         variable=self.window.mode, value=1, bg="#24273a",
                                         fg="#cad3f5", selectcolor="#24273a", activebackground="#24273a",
                                         activeforeground=theme["Overlay0"], cursor="hand2")
        self.normalMode.pack(side="left", padx=50)

        self.hardMode = tk.Radiobutton(self, text="Hard Mode", font=("Arial", 30, "bold"), variable=self.window.mode,
                                       value=2, bg="#24273a", fg="#cad3f5", selectcolor="#24273a",
                                       activebackground="#24273a", activeforeground=theme["Overlay0"], cursor="hand2")
        self.hardMode.pack(side="left", padx=50)


class GameFrame(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window, bg=theme["Base"])
        self.window = window
        self.start_time: float = time.time()
        self.now_numbers: str = ""
        self.question: str = ""
        self.done: bool = False
        self.num1: int = 0
        self.num2: int = 0
        self.awnsers: list[int] = []
        self.window.choise.set(0)
        self.op: str = ""
        self.indexOutOfBounds = False
        self.timeRemaining: str = ""
        self.timer = self.after(100, self.update_timer)
        self.window.capture = self.window.bind("<KeyPress>", self.key_press)
        self.ammount: int = 1

        self.infoL = tk.Frame(width=300, height=650, bg=theme["Base"], )
        self.infoL.pack_propagate(False)
        self.infoL.pack(side="left")

        self.calc = tk.Frame(width=500, height=650, bg=theme["Crust"], padx=10, pady=10)
        self.calc.pack_propagate(False)
        self.calc.pack(side="left", padx=0)

        self.infoR = tk.Frame(width=300, height=650, bg=theme["Base"], )
        self.infoR.pack_propagate(False)
        self.infoR.pack(side="left")

        self.new_question()

        self.CounterLabel = tk.Label(self.infoL, text=f"Frage: {self.window.counter}/{self.window.rounds}",
                                     font=("Arial", 32), width=20,
                                     height=2, bg=theme["Base"], fg=theme["Text"], pady=150)
        self.CounterLabel.pack()

        self.punkteLabel = tk.Label(self.infoL, text=f"Punkte: {self.window.punkte}/{(self.window.counter - 1) * 3}",
                                    font=("Arial", 32), width=20,
                                    height=2, bg=theme["Base"], fg=theme["Text"], pady=25)
        self.punkteLabel.pack()

        self.timeLabel = tk.Label(self.infoR,
                                  text=f"{(time.time() - self.start_time).__ceil__()} s/{self.timeRemaining}s",
                                  font=("Arial", 32),
                                  width=20,
                                  height=2, bg=theme["Base"], fg=theme["Text"], pady=150)
        self.timeLabel.pack()

        if self.window.mode.get() == 2:
            mode = "Hard"
        elif self.window.mode.get() == 1:
            mode = "Normal"
        else:
            mode = "Easy"

        self.modeLabel = tk.Label(self.infoR, text=f"{mode}\nmode", font=("Arial", 32), wraplength=150, width=20,
                                  height=2, bg=theme["Base"], fg=theme["Text"], pady=25, )
        self.modeLabel.pack()

        # calculator

        self.calc.columnconfigure(0, weight=1)
        self.calc.columnconfigure(1, weight=1)
        self.calc.columnconfigure(2, weight=1)
        self.calc.columnconfigure(3, weight=1)

        # text uses whole frame as its with length
        self.text = tk.Label(self.calc, font=("Arial", 32), width=19, height=2, bg="#005000", fg="#000000",
                             highlightbackground="#494d64", borderwidth=2, relief="groove")
        self.text.grid(columnspan=3, pady=20, sticky="nsew", padx=40, )
        self.question = f"{self.num1} {self.op} {self.num2} = "
        self.text.configure(text=self.question)

        if self.window.mode.get() == 0:
            self.choise0 = tk.Radiobutton(self.calc, text=f"{self.awnsers[0]}", font=("Arial", 30, "bold"),
                                          variable=self.window.choise,
                                          value=0, bg="#24273a", fg="#cad3f5", selectcolor="#24273a",
                                          activebackground="#24273a", activeforeground=theme["Overlay0"],
                                          cursor="hand2")
            self.choise0.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

            self.choise1 = tk.Radiobutton(self.calc, text=f"{self.awnsers[1]}", font=("Arial", 30, "bold"),
                                          variable=self.window.choise,
                                          value=1, bg="#24273a", fg="#cad3f5", selectcolor="#24273a",
                                          activebackground="#24273a", activeforeground=theme["Overlay0"],
                                          cursor="hand2")
            self.choise1.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

            self.choise2 = tk.Radiobutton(self.calc, text=f"", font=("Arial", 30, "bold"),
                                          variable=self.window.choise,
                                          value=2, bg="#24273a", fg="#cad3f5", selectcolor="#24273a",
                                          activebackground="#24273a", activeforeground=theme["Overlay0"],
                                          cursor="hand2")
            self.choise2.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)

            self.choise3 = tk.Radiobutton(self.calc, text=f"", font=("Arial", 30, "bold"),
                                          variable=self.window.choise,
                                          value=3, bg="#24273a", fg="#cad3f5", selectcolor="#24273a",
                                          activebackground="#24273a", activeforeground=theme["Overlay0"],
                                          cursor="hand2")
            self.choise3.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

            self.choise4 = tk.Radiobutton(self.calc, text=f"", font=("Arial", 30, "bold"),
                                          variable=self.window.choise,
                                          value=4, bg="#24273a", fg="#cad3f5", selectcolor="#24273a",
                                          activebackground="#24273a", activeforeground=theme["Overlay0"],
                                          cursor="hand2")
            self.choise4.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

            self.choise5 = tk.Radiobutton(self.calc, text=f"", font=("Arial", 30, "bold"),
                                          variable=self.window.choise,
                                          value=5, bg="#24273a", fg="#cad3f5", selectcolor="#24273a",
                                          activebackground="#24273a", activeforeground=theme["Overlay0"],
                                          cursor="hand2")
            self.choise5.grid(row=2, column=2, sticky="nsew", padx=10, pady=10)

            self.confirm = tk.Button(self.calc, text="Confirm", font=("Arial", 30), height=2,
                                     command=lambda: self.button_click("enter"),
                                     bg=theme["Overlay0"], fg=theme["Text"], borderwidth=2, relief="groove",
                                     activebackground=theme["Overlay2"])
            self.confirm.grid(row=3, column=0, sticky="nsew", pady=2, padx=4, columnspan=3)
        else:

            self.btn7 = tk.Button(self.calc, text="7", font=("Arial", 30), height=2,
                                  command=lambda: self.button_click(7),
                                  bg=theme["Overlay0"], fg=theme["Text"], borderwidth=2, relief="groove",
                                  activebackground=theme["Overlay2"])
            self.btn7.grid(row=1, column=0, sticky="nsew", pady=2, padx=4)

            self.btn8 = tk.Button(self.calc, text="8", font=("Arial", 30), height=2,
                                  command=lambda: self.button_click(8),
                                  bg=theme["Overlay0"], fg=theme["Text"], borderwidth=2, relief="groove",
                                  activebackground=theme["Overlay2"])
            self.btn8.grid(row=1, column=1, sticky="nsew", pady=2, padx=4)

            self.btn9 = tk.Button(self.calc, text="9", font=("Arial", 30), height=2,
                                  command=lambda: self.button_click(9),
                                  bg=theme["Overlay0"], fg=theme["Text"], borderwidth=2, relief="groove",
                                  activebackground=theme["Overlay2"])
            self.btn9.grid(row=1, column=2, sticky="nsew", pady=2, padx=4)

            self.btn4 = tk.Button(self.calc, text="4", font=("Arial", 30), height=2,
                                  command=lambda: self.button_click(4),
                                  bg=theme["Overlay0"], fg=theme["Text"], borderwidth=2, relief="groove",
                                  activebackground=theme["Overlay2"])
            self.btn4.grid(row=2, column=0, sticky="nsew", pady=2, padx=4)

            self.btn5 = tk.Button(self.calc, text="5", font=("Arial", 30), height=2,
                                  command=lambda: self.button_click(5),
                                  bg=theme["Overlay0"], fg=theme["Text"], borderwidth=2, relief="groove",
                                  activebackground=theme["Overlay2"])
            self.btn5.grid(row=2, column=1, sticky="nsew", pady=2, padx=4)

            self.btn6 = tk.Button(self.calc, text="6", font=("Arial", 30), height=2,
                                  command=lambda: self.button_click(6),
                                  bg=theme["Overlay0"], fg=theme["Text"], borderwidth=2, relief="groove",
                                  activebackground=theme["Overlay2"])
            self.btn6.grid(row=2, column=2, sticky="nsew", pady=2, padx=4)

            self.btn1 = tk.Button(self.calc, text="1", font=("Arial", 30), height=2,
                                  command=lambda: self.button_click(1),
                                  bg=theme["Overlay0"], fg=theme["Text"], borderwidth=2, relief="groove",
                                  activebackground=theme["Overlay2"])
            self.btn1.grid(row=3, column=0, sticky="nsew", pady=2, padx=4)

            self.btn2 = tk.Button(self.calc, text="2", font=("Arial", 30), height=2,
                                  command=lambda: self.button_click(2),
                                  bg=theme["Overlay0"], fg=theme["Text"], borderwidth=2, relief="groove",
                                  activebackground=theme["Overlay2"])
            self.btn2.grid(row=3, column=1, sticky="nsew", pady=2, padx=4)

            self.btn3 = tk.Button(self.calc, text="3", font=("Arial", 30), height=2,
                                  command=lambda: self.button_click(3),
                                  bg=theme["Overlay0"], fg=theme["Text"], borderwidth=2, relief="groove",
                                  activebackground=theme["Overlay2"])
            self.btn3.grid(row=3, column=2, sticky="nsew", pady=2, padx=4)

            self.btn0 = tk.Button(self.calc, text="0", font=("Arial", 30), height=2,
                                  command=lambda: self.button_click(0),
                                  bg=theme["Overlay0"], fg=theme["Text"], borderwidth=2, relief="groove",
                                  activebackground=theme["Overlay2"])
            self.btn0.grid(row=4, column=1, sticky="nsew", pady=2, padx=4)

            self.btn_del = tk.Button(self.calc, text="C", font=("Arial", 30), height=2,
                                     command=lambda: self.button_click("del"), bg=theme["Overlay0"], fg=theme["Text"],
                                     borderwidth=2, relief="groove", activebackground=theme["Overlay2"])
            self.btn_del.grid(row=4, column=0, sticky="nsew", pady=2, padx=4)

            self.btn_enter = tk.Button(self.calc, text="=", font=("Arial", 30), height=2,
                                       command=lambda: self.button_click("enter"), bg=theme["Overlay0"],
                                       fg=theme["Text"],
                                       borderwidth=2, relief="groove", activebackground=theme["Overlay2"])
            self.btn_enter.grid(row=4, column=2, sticky="nsew", pady=2, padx=4)

        self.infoL.pack()
        self.calc.pack()
        self.infoR.pack()

    def key_press(self, event):
        key = event.char
        if key in "1234567890" and not self.window.mode.get() == 0:
            self.button_click(int(key))
        elif key == "\r":
            self.button_click("enter")
        elif key == "\x08" and not self.window.mode.get() == 0:
            self.button_click("del")

    def update_timer(self):
        if time.time() - self.start_time < 10:
            self.timeRemaining = "10"
        elif time.time() - self.start_time < 20:
            self.timeRemaining = "20"
        else:
            self.timeRemaining = "∞"

        self.timeLabel.configure(text=f"{(time.time() - self.start_time).__ceil__()} s/{self.timeRemaining}s")
        self.timer = self.after(100, self.update_timer)

    def new_question(self):
        self.num1, self.num2, self.op = get_random_question(self.window.mode.get())
        self.question = f"{self.num1} {self.op} {self.num2} = "

        if self.window.mode.get() == 0:
            self.awnsers = []
            self.awnsers.append(int(eval(self.question[:-2])))
            for i in range(self.ammount):
                self.awnsers.append(fake_answer(self.awnsers[0]))
            random.shuffle(self.awnsers)

    def button_click(self, number):

        if self.window.mode.get() == 0:
            if self.window.choise.get() > self.ammount:
                self.indexOutOfBounds = True
            else:
                self.indexOutOfBounds = False
                self.now_numbers = str(self.awnsers[self.window.choise.get()])



        if number != "del" and number != "enter" and not self.done:
            self.now_numbers += str(number)
            self.text.configure(text=self.question + self.now_numbers)
        elif number == "del" and not self.done:
            self.now_numbers = self.now_numbers[:-1]
            self.text.configure(text=self.question + self.now_numbers)
        elif number == "enter" and not self.done and self.now_numbers != "" and not self.indexOutOfBounds:
            self.window.counter += 1
            self.after_cancel(self.timer)
            self.timeLabel.configure(text=f"{(time.time() - self.start_time).__round__(2)} s/{self.timeRemaining}s")
            if test_answer(self.num1, self.num2, self.op, int(self.now_numbers)):
                self.text.configure(text=f"Richtig\n{self.question}{self.now_numbers}")
                if (time.time() - self.start_time) < 10:
                    self.window.punkte += 3
                elif (time.time() - self.start_time) < 20:
                    self.window.punkte += 2
                else:
                    self.window.punkte += 1
                if self.ammount < 6:
                    self.ammount += 1
            else:
                self.text.configure(
                    text=f"Falsch\nrichtig: {self.question}{int(eval(f'{self.num1} {self.op} {self.num2}')).__round__(2)}")
                if self.ammount > 1:
                    self.ammount -= 1
            self.done = True
            self.punkteLabel.configure(text=f"Punkte: {self.window.punkte}/{(self.window.counter - 1) * 3}")
            self.window.startOfGame += (time.time() - self.start_time).__round__(2)
            if self.window.mode.get() == 0:
                self.choise0.configure(text="")
                self.choise1.configure(text="")
                self.choise2.configure(text="")
                self.choise3.configure(text="")
                self.choise4.configure(text="")
                self.choise5.configure(text="")

        elif number == "enter" and self.done:

            self.now_numbers = ""
            self.CounterLabel.configure(text=f"Frage: {self.window.counter}/{self.window.rounds}")
            self.new_question()
            if self.window.mode.get() == 0:
                self.choise0.configure(text=self.awnsers[0])
                self.choise1.configure(text=self.awnsers[1])
                if self.ammount > 1:
                    self.choise2.configure(text=self.awnsers[2])
                if self.ammount > 2:
                    self.choise3.configure(text=self.awnsers[3])
                if self.ammount > 3:
                    self.choise4.configure(text=self.awnsers[4])
                if self.ammount > 4:
                    self.choise5.configure(text=self.awnsers[5])

            self.text.configure(text=self.question)
            self.start_time = time.time()
            self.timer = self.after(100, self.update_timer)
            self.done = False
            if self.window.counter >= self.window.rounds:
                self.calc.destroy()
                self.infoL.destroy()
                self.infoR.destroy()
                self.window.switch(EndFrame)


class EndFrame(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.window = window
        self.window.title("Ende")
        self.configure(bg=theme["Base"], padx=10, pady=10)

        if self.window.mode.get() == 2:
            mode = "Hard"
        elif self.window.mode.get() == 1:
            mode = "Normal"
        else:
            mode = "Easy"

        self.lable = tk.Label(self, text=f"Vorbei\nDu hast auf {mode}-mode {self.window.punkte}"
                                         f" punkte erhalten\nDu hast dafür nur {self.window.startOfGame}s gebraucht",
                              font=("Arial", 30),
                              bg="#24273a", fg="#cad3f5", borderwidth=2, relief="groove", padx=10, pady=10, height=3,
                              width=40, anchor="center", justify="center")
        self.lable.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=200, padx=4)

        self.button = tk.Button(self, text="Neues Spiel", font=("Arial", 30), height=2, command=lambda: self.restart(),
                                bg=theme["Base"], fg=theme["Text"], borderwidth=2, relief="groove",
                                activebackground=theme["Overlay2"])
        self.button.grid(row=2, column=0, columnspan=2, sticky="nsew", pady=2, padx=8)

        self.button = tk.Button(self, text="Beenden", font=("Arial", 30), height=2,
                                command=lambda: self.window.destroy(), bg=theme["Base"], fg=theme["Text"],
                                borderwidth=2, relief="groove", activebackground=theme["Overlay2"])
        self.button.grid(row=2, column=2, columnspan=2, sticky="nsew", pady=2, padx=8)

    def restart(self):
        self.window.punkte = 0
        self.window.counter = 1
        self.window.switch(StartFrame)


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
