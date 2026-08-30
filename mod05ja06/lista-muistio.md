Operaatio	Tarkoitus	Esimerkki
append	lisää alkion listan loppuun	nimet.append(“Matti”)
remove	poistaa alkion ensimmäisen ilmentymän listasta	nimet.remove(“Pekka”)
insert	lisää alkion haluttuun kohtaan, ennen alkiota, jonka indeksi vastaa ensimmäistä argumenttia	nimet.insert(4, “Teppo”)
extend	liittää toisen listan ensimmäiseen listaan	toisetNimet = [“Allu”,”Ninni”]
nimet.extend(toisetNimet)
index	palauttaa alkion ensimmäisen sijainnin indeksin	monesko = nimet.index(“Olga”)
in	testaa, esiintyykö alkio listassa	if “Matti” in nimet:
    “Matti löytyi”
sort	lajittelee listan alkiot aakkos- tai suuruusjärjestykseen	luvut.sort()