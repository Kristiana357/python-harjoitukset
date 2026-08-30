"""
Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. 
Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
"""

import random


oikein_arvaus = random.randint(1, 10)

arvaus = int(input("Arvaa kokonaisluku väliltä 1..10: "))

while arvaus != oikein_arvaus:
    if arvaus < oikein_arvaus:
        print("Liian pieni arvaus")
    else:
        print("Liian suuri arvaus")
    arvaus = int(input("Arvaa kokonaisluku väliltä 1..10: "))

print("Oikein!")