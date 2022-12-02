import turtle
import random

print("ze tutaj mamy prztlumoczone funkcje zolwia(turtle)"
      "mozesz z tego uzywac w kai sposob"
      "jak nie potrafisz to uzyc pomoc()")
def pomoc():
    hint = "tu mogę zrobić plik txt i bedzie go czytal"
    return hint

def czyszczenie_obrazu():
    return turtle.reset()

def usun():
    return turtle.clear()

class Nazwij:
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
                  " Na przykład:Imie_żółwia.personalizacja(\"turtle\", \"czerwony\")"
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

