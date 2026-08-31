"""Tee kansioon ohjelma, joka kysyy pelaajan nimen ja iän, tallentaa nämä muuttujiin ja tulostaa konsoliin."""

nimi = input("Anna pelaajan nimi: ")
ikä = int(input("Anna pelaajan ikä: "))

print("Pelaajan nimi:", nimi)
print("Pelaajan ikä:", ikä)

"""Muokkaa peliprojektiohjelmaa niin, että jos käyttäjä syöttää iän, joka on alle 12 v., 
ohjelma ilmoittaa alaikäisyydestä ja sammuu. Muussa tapauksessa ohjelma tervehtii käyttäjää, 
tulostaa päävalikon ja kysyy komentoja, kunnes käyttäjä kirjoittaa “lopeta”.
Lisää muutama keksitty komento, jotka antavat keskenään erilaisen tulosteen konsoliin. 
Komennon jälkeen tulostetaan valikko aina uudelleen."""

if ikä < 12:
    print("Olet alaikäinen. Ohjelma sammuu.")
else:
    print("Tervetuloa, " + nimi + "!")
    while True:
        print("\n--- PÄÄVALIKKO ---")
        print("1 - pelaa")
        print("2 - pisteet")
        print("lopeta - lopeta peli")

        komento = input("Anna komento: ")
        if komento == "1":
            print("Aloitetaan peli!")
        elif komento == "2":
            print("Tässä ovat pisteesi: 100")
        elif komento == "lopeta":
            print("Lopetetaan peli.")
            break
        else:
            print("Tuntematon komento.")