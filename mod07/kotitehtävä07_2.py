import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)


maksimi = int(input("Anna nopan tahkojen määrä: "))

silmaluku = 0

while silmaluku != maksimi:
    silmaluku = heita_noppaa(maksimi)
    print(silmaluku)