"""Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän
käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista 
jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa."""


def muunna_litroiksi(gallona):
    return gallona * 3.785

while True:
    gallona = float(input("Anna bensiinin määrä Yhdysvaltain nestegallonoina (negatiivinen luku lopettaa): "))
    if gallona < 0:
        break
    litraa = muunna_litroiksi(gallona)
    print(litraa)