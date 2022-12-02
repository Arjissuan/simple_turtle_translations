import turtle
from random import *

def powitanie():
    hello = "Witaj w naszym tłumaczeniu pakietu turtle.\n" \
            "Razem z nim nauczymy cię podstaw programowania\n" \
            "Zacznijmy od wpisania funkcji: pomoc()\n" \
            "Możesz ją wywołać w każdej chwili.\n" \
            "Najważniejsze aby nie zrażać się błędami, zwłaszcza w programowaniu\n" \
            "Każdy błąd nauczy Cię czegoś nowego.\n"
    return hello
def pomoc():
    with open("instrukcja.txt", "r") as file:
        hint = file
    return hint

def czyszczenie_obrazu():
    return turtle.reset()

def usun():
    return turtle.clear()

class Imie_mojego_zolwia:
    kolory_linii = ["czerwony", "zielony", "czarny","losowy"]
    shapes = ["turtle"]
    def __init__(self):
        self.zolw = turtle.Turtle()

    def personalizacja(self, shape, kolor):
        try:
            self.zolw.shape(str(shape))
            tru_clours = ["red", "green", "black", "yellow", ]
            if kolor in ["czerwony", "zielony", "czarny", "żółty",]:
                self.zolw.color(tru_clours[self.kolory_linii.index(kolor)])
            elif kolor == "losowy":
                self.zolw.color(random.choice(("green", "yellow", "red", "black")))
            else:
                print("Zły kolor, dostępne to {}".format(self.kolory_linii))
        except:
            print("Ta funkcja przyjmuje wartości w postaci danych string.\n"
                  " Na przykład:Marek.personalizacja(\"turtle\", \"czerwony\")"
                  f"dostepne kolory i kształy:{self.kolory_linii}, {self.shapes}")

    def w_lewo(self, ile):
        self.zolw.left(ile)

    def do_przodu(self, ile):
        self.zolw.forward(ile)

    def w_prawo(self, ile):
        self.zolw.right(ile)

    def osmiokat(self):
        for item in range(9):
            self.zolw.left(40)
            self.zolw.forward(30)

    def wielokat(self, L_or_P, angle, speed, many):
        for item in range(many):
            if L_or_P== "prawo" or L_or_P == "w_prawo":
                self.zolw.right(angle)
                self.zolw.forward(speed)
            elif L_or_P == "lewo" or L_or_P == "w_lewo":
                self.zolw.left(angle)
                self.zolw.forward(speed)
            else:
                return "Niepoprawnie uzyta funkcja, przyjmuje ona 4 argumenty, pierwszym określasz czy żółw ma iść w prawo czy lewo\n" \
                       "kolejne określają kąt i jakie dlugie odcinki ma przebyc żółw." \
                       "Na_przykład.wielokat(lewo, 2,3,99)"



    def pen(self, rysowanie=True, kolor=None):
        try:
            if rysowanie in ["tak", "rysuj", "maluj", True, "True", "true"]:
                self.zolw.pendown()
            elif rysowanie in ["nie", "przestan", "stop", "niemaluj", False, "false", 'False']:
                self.zolw.penup()

            if kolor==None:
                pass
        except:
            print("Ta funkcja jest aby włączyć lub wyłączyć rysowanie, uzyj jej Imie.pen() gdzie argumenty to True aby rysowac i false aby przestac.")
