import random

# Choisi un mot
mots = []
with open("mots.txt") as fl:
    for l in fl:
        mots.append(l.rstrip("\n"))
mot = random.choice(mots)

# Variable cle
lettres = []
faux = 0
trouve = False
corps_plein = ["O", "/", "|", "\\", "/", "\\"]
corps = [" ", " ", " ", " ", " ", " "]

while not trouve:
    trouve = True
    print(" +---+")
    print(" |   |")
    print(" |   {}".format(corps[0]))
    print(" |  {}{}{}".format(corps[1], corps[2], corps[3]))
    print(" |  {} {}".format(corps[4], corps[5]))
    print("_|_")
    print("| |")
    for l in mot:
        if l in lettres:
            print(l, end=" ")
        else:
            trouve = False
            print("_", end=" ")
    print()
    print("Lettres utilisées - ", end="")
    for l in lettres:
        print(l, end=" | ")
    print()

    if faux > 5:
        print("Oh non :( Tu as perdu...")
        print("Le mot était : {}".format(mot))
        break

    if trouve:
        print("Bravo ! Tu viens de remporter La partie !")
        break

    lettre = input("Entez une lettre: ")
    lettres.append(lettre)

    if lettre not in mot:
        corps[faux] = corps_plein[faux]
        faux += 1