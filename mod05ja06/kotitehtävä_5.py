"""
Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
(Oikea käyttäjätunnus on python ja salasana rules).
"""

oikea_tunnus = "python"
oikea_salasana = "rules"

input_tunnus = input("Anna käyttäjätunnus: ")
input_salasana = input("Anna salasana: ")

yritykset = 0
yritukset_max = 5

while (input_tunnus != oikea_tunnus or input_salasana != oikea_salasana) and yritykset < yritukset_max:
    print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")
    input_tunnus = input("Anna käyttäjätunnus: ")
    input_salasana = input("Anna salasana: ")
    yritykset = yritykset + 1


if yritykset >= yritukset_max:
    print("Pääsy evätty.")
else:
    print("Tervetuloa!")