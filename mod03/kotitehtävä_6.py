import random

kolminumeroinen = (
    random.randint (0, 9),
    random.randint (0, 9),
    random.randint (0, 9)
)

nelinumeroinen = (
    random.randint(1, 6),
    random.randint(1, 6),
    random.randint(1, 6),
    random.randint(1, 6)
)
print("Kolmenumeroinen koodi:", "".join(map(str, kolminumeroinen)))
print("Neljämeroinen koodi:", "".join(map(str, nelinumeroinen)))