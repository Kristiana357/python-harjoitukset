import random

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


"""Kehitä peliprojektia eteenpäin: Luo jokaiselle päävalikon toiminnolle (joita vähintään kolme) oma funktio, 
joka suoritetaan, kun käyttäjä valitsee kyseisen toiminnon.
Yhden funktion pitää kysyä käyttäjältä asioita (esim. esine), jotka lisätään listamuuttujaan.
Toisen funktion pitää tulostaa listan sisältö käyttäjälle.
Muut toiminnot voi ideoida ja toteuttaa vapaasti.
"""

esineet = []
koneen_valinta = None

def näytä_päävalikko():
    print("\n--- PÄÄVALIKKO ---")
    print("1 - pelaa")
    print("2 - näytä pelaajan tiedot")
    print("lopeta - lopeta peli")


def näytä_pelivalikko():
    print("\n--- PELIVALIKKO ---")
    print("1 - lisää esine")
    print("2 - tulosta esineet")
    print("3 - arvaa esine, jonka kone on valinnut")
    print("lopeta - lopeta peli")


def käsittele_esine():
    esine = input("Anna esine: ")
    esineet.append(esine)


def tulosta_esineet():
    if len(esineet) == 0:
        print("Ei ole esineitä tulostettavaksi.")
        return
    print("Tässä ovat esineet:")
    for esine in esineet:
        print("- " + esine)


def tulosta_pelajan_tiedot():
    print("Pelaajan tiedot:")
    print("Nimi: " + nimi)
    print("Ikä: " + str(ikä))


def valitse_koneen_esine():
    esineiden_maara = len(esineet)
    if esineiden_maara == 0:
        print("Ei ole esineitä valittavaksi.")
        return None
    return esineet[random.randint(0, esineiden_maara - 1)]


def kysy_arvaus():
    arvaus = input("Arvaa esine: ")
    esineiden_maara = len(esineet)
    if esineiden_maara == 0:
        print("Ei ole esineitä arvattavaksi.")
        return

    global koneen_valinta
    
    if arvaus in esineet and arvaus == koneen_valinta:
        print("Oikein! Esine löytyi listasta.")
        koneen_valinta = None
    else:
        print("Väärin! Esine ei löytynyt listasta tai se ei ollut koneen valitsema esine.")


def poista_pelin_tila():
    global esineet, koneen_valinta
    esineet = []
    koneen_valinta = None
        

if ikä < 12:
    print("Olet alaikäinen. Ohjelma sammuu.")
else:
    print("Tervetuloa, " + nimi + "!")
    while True:
        näytä_päävalikko()

        päävalikko_komento = input("Anna komento: ")
        
        if päävalikko_komento == "1":
            print("Aloitetaan peli!")

            while True:
                näytä_pelivalikko()

                pelivalikko_komento = input("Anna komento: ")
                if pelivalikko_komento == "1":
                    käsittele_esine()
                elif pelivalikko_komento == "2":
                    tulosta_esineet()
                elif pelivalikko_komento == "3":
                    if koneen_valinta is None:
                        koneen_valinta = valitse_koneen_esine()
                    kysy_arvaus()
                elif pelivalikko_komento == "lopeta":
                    poista_pelin_tila()
                    print("Siirrytään päävalikkoon.")
                    break
                else:
                    print("Tuntematon komento.")
        elif päävalikko_komento == "2":
            tulosta_pelajan_tiedot()
        elif päävalikko_komento == "lopeta":
            poista_pelin_tila()
            print("Lopetetaan peli.")
            break
        else:
            print("Tuntematon komento.")     

