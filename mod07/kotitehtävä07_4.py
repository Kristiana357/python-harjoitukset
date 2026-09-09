"""Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. 
Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma, 
jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan."""

def summa(luvut):
    summa = 0

    for luku in luvut:
        summa = summa + luku

    return summa


luvut = [2, 5, 3]

tulos = summa(luvut)

print(tulos)