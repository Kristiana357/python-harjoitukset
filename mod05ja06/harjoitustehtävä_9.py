nimet = []

nimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
nimet.append(nimi)
while nimi != "":
    valinta = input("haluatko lisätä vai poistaa (l taii p)")
    if(valinta == "l"):
        nimi = input("Anna seurava nimi tai lopeta painamalla Enter:")
        nimet.append(nimi)

    else:
        nimi = input ("Anna seurava nimi poistettavaksi tai lopeta painamalla Enter: ")
        nimet.remove(nimi)

print(nimet)