import turtle
import random

def powitanie():
    hello = "Witaj w naszym tłumaczeniu pakietu turtle.\n" \
            "Razem z nim nauczymy cię podstaw programowania\n" \
            "Zacznijmy od wpisania funkcji: pomoc()\n" \
            "Możesz ją wywołać w każdej chwili.\n" \
            "Najważniejsze aby nie zrażać się błędami, zwłaszcza w programowaniu\n" \
            "Każdy błąd nauczy Cię czegoś nowego.\n"
    return hello
def pomoc():
    with open("instrukcja.txt", "r", encoding='utf-8') as file:
        for item in file.read().splitlines():
            print(item)


class Imie_mojego_zolwia:
    kolory_linii = ["czerwony", "fioletowy","zielony", "czarny","żółty", "pomarańczowy","losowy"]
    tru_clours = ["red", "purple","green", "black", "yellow", "orange", ]
    shapes = ["turtle", "arrow", "classic", "circle"]

    def __init__(self):
        self.zolw = turtle.Turtle()

    def personalizacja(self, shape, kolor):
        try:
            self.zolw.shape(str(shape))

            if kolor in self.kolory_linii:
                self.zolw.color(self.tru_clours[self.kolory_linii.index(kolor)])
            elif kolor == "losowy":
                self.zolw.color(random.choice(self.kolory_linii))
            else:
                return ("Ta funkcja przyjmuje wartości w postaci danych string.\n"
                        " Na przykład:Marek.personalizacja(\"turtle\", \"czerwony\")"
                        f"dostepne kolory i kształy:{self.kolory_linii}, {self.shapes}")
        except:
            return ("Ta funkcja przyjmuje wartości w postaci danych string.\n"
                  " Na przykład:Marek.personalizacja(\"turtle\", \"czerwony\")\n"
                  f"dostepne kolory i kształy:{self.kolory_linii}, {self.shapes}")

    def w_lewo(self, ile):
        self.zolw.left(ile)

    def do_przodu(self, ile):
        self.zolw.forward(ile)

    def w_prawo(self, ile):
        self.zolw.right(ile)

    def do_tylu(self, ile):
        self.zolw.backward(ile)

    def osmiokat(self):
        for item in range(9):
            self.zolw.left(40)
            self.zolw.forward(30)

    def wielokat(self, L_or_P, angle, speed, many):
        if type(angle) != int or type(speed) != int or type(many) != int:
            return "Niepoprawnie uzyta funkcja, przyjmuje ona 4 argumenty, pierwszym określasz czy żółw ma iść w prawo czy lewo\n" \
                       "kolejne określają kąt i jakie dlugie odcinki ma przebyc żółw.\n" \
                       "Na_przykład.wielokat(lewo, 2,3,99)"
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

    def pen(self, rysowanie, kolor):
        if rysowanie in ["tak", "rysuj", "maluj", True, "True", "true"]:
            self.zolw.pendown()
        elif rysowanie in ["nie", "przestan", "stop", "niemaluj", False, "false", 'False']:
            self.zolw.penup()
        else:
            return "Ta funkcja jest aby włączyć lub wyłączyć rysowanie, uzyj jej Imie.pen() gdzie argumenty to True aby rysowac i false aby przestac\n." \
                   f"Kolory zaś to {self.kolory_linii}"
        if kolor == None:
            pass
        elif kolor in self.kolory_linii:
            self.zolw.pencolor(self.tru_clours[self.kolory_linii.index(kolor)])
        else:
            return "Ta funkcja jest aby włączyć lub wyłączyć rysowanie, uzyj jej Imie.pen() gdzie argumenty to True aby rysowac i false aby przestac\n." \
                   f"Kolory zaś to {self.kolory_linii}"
    def znaczek(self):
        self.zolw.stamp()

    def benzen(self):
        for x in range(180):
            self.zolw.pencolor(self.tru_clours[x%6])
            self.zolw.width(x//100 +1)
            self.zolw.forward(x)
            self.zolw.left(59)

    def kwadrat(self):
        for i in range(4):
            self.zolw.forward(40)
            self.zolw.right(90)

    def sqrfunc(self, size):
        for i in range(4):
            self.zolw.fd(size)
            self.zolw.lt(size)
            size = size -5

    def konczymy(self):
        turtle.bye()
        exit()

    def resetowanie(self):
        self.zolw.reset()

    def usun_obrazek(self):
        self.zolw.clear()



