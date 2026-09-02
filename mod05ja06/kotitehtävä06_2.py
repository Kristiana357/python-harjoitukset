"""Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
 kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
 Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. 
 Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True."""

lukuja = []

luku = input("Anna luku tai lopeta painamalla Enter: ")
while luku != "":
    lukuja.append(int(luku))
    luku = input("Anna luku tai lopeta painamalla Enter: ")

lukuja.sort(reverse=True)
print("Viisi suurinta lukua:", lukuja[:5])
