import turtle
import random
from script import *


if __name__ == "__main__":
    try:
        print(powitanie())
        Marek = Imie_mojego_zolwia()
    except NameError:
        print("Niepoprawna komenda")

