
luvut = []

luku = input("Anna luku tai lopeta painamalla Enter: ")
while luku != "":
    luvut.append(int(luku))
    luku = input("Anna luku tai lopeta painamalla Enter: ")

print("Suurin luku:", max(luvut))
print("Pienin luku:", min(luvut))