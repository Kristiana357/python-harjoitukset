leivisköinä = float(input("Anna leiviskät: "))
nauloina = float(input("Anna naulat: "))
luoteina = float(input("Anna luodit: "))


grammat = ((leivisköinä * 20 + nauloina) * 32 + luoteina) * 13.3
kilos = int(grammat // 1000)
grams = round(grammat % 1000, 2)

print("Massa nykymittojen mukaan:")
print(str(kilos) + " kilogrammaa ja " + str(grams) + " grammaa.")