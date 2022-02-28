import random
# Random gets inported here.

import sys, os
# System gets inported here.

import time
# Time gets imported here.

os.system('cls')
# The console gets cleared.

print("------------------------------------------------------------------------------------------")
print(" ")
print("Hallo, welkom bij Yahtzee.")
print("Het doel is om een zo hoog mogelijke score te krijgen door bepaalde patronen of volgorde's te gooien")
print("Wanneer je de dobbelstenen gooit kan je kiezen of je ze wilt houden of sommige dobbelstenen opnieuw wilt gooien")
print("Per Beurt mag je maximaal drie keer gooien.")
print("(Gemaakt door Niels van Rheenen, V4D, Het Streek Lyceum.)")
print(" ")
print("------------------------------------------------------------------------------------------")
print(" ")
# Printing the explaination and rules of the game.

time.sleep(5)
# Wating five seconds.

os.system('cls')
# Clearing the console

dobbelStenen = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
# Making a list with all the dices.

rnd1 = random.choice(dobbelStenen)
rnd2 = random.choice(dobbelStenen)
rnd3 = random.choice(dobbelStenen)
rnd4 = random.choice(dobbelStenen)
rnd5 = random.choice(dobbelStenen)

currentDobbelstenen = [rnd1, rnd2, rnd3, rnd4, rnd5]
# Picking random dices from the list and putting the five random dices in a new list.

print("------------------------------------------------------------------------------------------")
print("Dit zijn je eerste dobbelstenen:")
print(currentDobbelstenen)
print("------------------------------------------------------------------------------------------")
print(" ")
# Printing the random dices.

houden = input("Wil je je dobbelstenen houden? Voer ja of nee in. ")

beurt = 0

while houden == "nee":
    print(" ")
    print("ok we gaan verder")
    print(" ")

    wisselen1 = input("wil je dobbelsteen 1 wisselen, voer ja of nee in? ")
    wisselen2 = input("wil je dobbelsteen 2 wisselen, voer ja of nee in? ")
    wisselen3 = input("wil je dobbelsteen 3 wisselen, voer ja of nee in? ")
    wisselen4 = input("wil je dobbelsteen 4 wisselen, voer ja of nee in? ")
    wisselen5 = input("wil je dobbelsteen 5 wisselen, voer ja of nee in? ")

    if wisselen1 == "ja":
        currentDobbelstenen[0] = random.choice(dobbelStenen)
    if wisselen2 == "ja":
        currentDobbelstenen[1] = random.choice(dobbelStenen)
    if wisselen3 == "ja":
        currentDobbelstenen[2] = random.choice(dobbelStenen)
    if wisselen4 == "ja":
        currentDobbelstenen[3] = random.choice(dobbelStenen)
    if wisselen5 == "ja":
        currentDobbelstenen[4] = random.choice(dobbelStenen)

    print(" ")
    print("------------------------------------------------------------------------------------------")
    print("Dit zijn je nieuwe dobbelstenen:")
    print(currentDobbelstenen)
    print("------------------------------------------------------------------------------------------")
    print(" ")

    beurt = beurt + 1

    if beurt == 2:
        houden = "ja"
    else:
        houden = input("Wil je je dobbelstenen houden? Voer ja of nee in. ")

    print(" ")
    print("------------------------------------------------------------------------------------------")
    print("Dit zijn je dobbelstenen uit eindelijk geworden:")
    print(currentDobbelstenen)
    print("------------------------------------------------------------------------------------------")
    print(" ")

if currentDobbelstenen.count("1️⃣") == 3 or currentDobbelstenen.count("2️⃣") == 3 or currentDobbelstenen.count("3️⃣") == 3 or currentDobbelstenen.count("4️⃣") == 3 or currentDobbelstenen.count("5️⃣") == 3 or currentDobbelstenen.count("6️⃣") == 3:
    threeOfAKind = True
else: threeOfAKind = False

if currentDobbelstenen.count("1️⃣") == 4 or currentDobbelstenen.count("2️⃣") == 4 or currentDobbelstenen.count("3️⃣") == 4 or currentDobbelstenen.count("4️⃣") == 4 or currentDobbelstenen.count("5️⃣") == 4 or currentDobbelstenen.count("6️⃣") == 4:
    fourOfAKind = True
else: fourOfAKind = False

if currentDobbelstenen.count("1️⃣") == 5 or currentDobbelstenen.count("2️⃣") == 5 or currentDobbelstenen.count("3️⃣") == 5 or currentDobbelstenen.count("4️⃣") == 5 or currentDobbelstenen.count("5️⃣") == 5 or currentDobbelstenen.count("6️⃣") == 5:
    Yahtzee = True
else: Yahtzee = False

if ('1️⃣' and '2️⃣' and '3️⃣' and '4️⃣') or ('2️⃣' and '3️⃣' and '4️⃣' and '5️⃣') or ('3️⃣' or'4️⃣' and '5️⃣' and '6️⃣') in currentDobbelstenen:
    smallStreet = True
else: smallStreet = False

if ('1️⃣' and '2️⃣' and '3️⃣' and '4️⃣' and '5️⃣') or ('2️⃣' and '3️⃣' and '4️⃣' and '5️⃣' and '6️⃣') in currentDobbelstenen:
    bigStreet = True
else: bigStreet = False

if (currentDobbelstenen.count("1️⃣") == 2 or currentDobbelstenen.count("2️⃣") == 2 or currentDobbelstenen.count("3️⃣") == 2 or currentDobbelstenen.count("4️⃣") == 2 or currentDobbelstenen.count("5️⃣") == 2 or currentDobbelstenen.count("6️⃣") == 2) and (currentDobbelstenen.count("1️⃣") == 3 or currentDobbelstenen.count("2️⃣") == 3 or currentDobbelstenen.count("3️⃣") ==3 or currentDobbelstenen.count("4️⃣") == 3 or currentDobbelstenen.count("5️⃣") == 3 or currentDobbelstenen.count("6️⃣") == 3):
    fullHouse = True
else: fullHouse = False


if (threeOfAKind == True and fourOfAKind == False and Yahtzee == False and smallStreet == False and bigStreet == False and fullHouse == False):
    print("You Have Three of a kind!")
elif (threeOfAKind == False and fourOfAKind == True and Yahtzee == False and smallStreet == False and bigStreet == False and fullHouse == False):
    print("You Have Four of a kind!")
elif (threeOfAKind == False and fourOfAKind == False and Yahtzee == True and smallStreet == False and bigStreet == False and fullHouse == False):
    print("You Have Yahtzee!")
elif (threeOfAKind == False and fourOfAKind == False and Yahtzee == False and smallStreet == True and bigStreet == False and fullHouse == False):
    print("You Have Small Street!")
elif (threeOfAKind == False and fourOfAKind == False and Yahtzee == False and smallStreet == False and bigStreet == True and fullHouse == False):
    print("You Have Big Street!")
elif (threeOfAKind == False and fourOfAKind == False and Yahtzee == False and smallStreet == False and bigStreet == False and fullHouse == True):
    print("You Have Full House!")
else:
    print("You have no results.")