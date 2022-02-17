from pickle import FALSE
from pickletools import read_unicodestring1
import random
from re import X
# Hier word een module ge-inporteerd waarmee je makkelijk random getallen kan genereren.

import sys, os
# Hier word os ge-inporteerd zodat je de command-line kan leegmaken.

import time
# Hier word time ge-inporteerd zodat je python kan laten wachten.

from collections import Counter
# Hier word Counter ge-inporteerd

os.system('cls')

print("-----------------------")

naam = input("wat is je naam? ")

os.system('cls')
# hier word het scherm leeg gemaakt

print("------------------------------------------------------------------------------------------")
print(" ")
print("Hallo " + naam + ", welkom bij Yahtzee.")
print("Het doel is om een zo hoog mogelijke score te krijgen door bepaalde patronen of volgorde's te gooien")
print("Wanneer je de dobbelstenen gooit kan je kiezen of je ze wilt houden of sommige dobbelstenen opnieuw wilt gooien")
print("Per Beurt mag je maximaal drie keer gooien.")
print("(Gemaakt door Niels van Rheenen, V4D, Het Streek Lyceum.)")
print(" ")
print("------------------------------------------------------------------------------------------")
print(" ")

time.sleep(5)

os.system('cls')

dobbelStenen = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]

rnd1 = random.choice(dobbelStenen)
rnd2 = random.choice(dobbelStenen)
rnd3 = random.choice(dobbelStenen)
rnd4 = random.choice(dobbelStenen)
rnd5 = random.choice(dobbelStenen)

currentDobbelstenen = [rnd1, rnd2, rnd3, rnd4, rnd5]

print("------------------------------------------------------------------------------------------")
print("Dit zijn je eerste dobbelstenen:")
print(currentDobbelstenen)
print("------------------------------------------------------------------------------------------")
print(" ")

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

    if beurt == 3:
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
    print("Three of a kind is found!")

if currentDobbelstenen.count("1️⃣") == 4 or currentDobbelstenen.count("2️⃣") == 4 or currentDobbelstenen.count("3️⃣") == 4 or currentDobbelstenen.count("4️⃣") == 4 or currentDobbelstenen.count("5️⃣") == 4 or currentDobbelstenen.count("6️⃣") == 4:
    print("Four of a kind is found!")

if currentDobbelstenen.count("1️⃣") == 5 or currentDobbelstenen.count("2️⃣") == 5 or currentDobbelstenen.count("3️⃣") == 5 or currentDobbelstenen.count("4️⃣") == 5 or currentDobbelstenen.count("5️⃣") == 5 or currentDobbelstenen.count("6️⃣") == 5:
    print("Yahtzee of a kind is found!")

if '1️⃣' and '2️⃣' and '3️⃣' and '4️⃣' in currentDobbelstenen:
    print("Small House is found!")

if '1️⃣' and '2️⃣' and '3️⃣' and '4️⃣' and '5️⃣' in currentDobbelstenen:
    print("Small House is found!")

if (currentDobbelstenen.count("1️⃣") == 2 or currentDobbelstenen.count("2️⃣") == 2 or currentDobbelstenen.count("3️⃣") == 2 or currentDobbelstenen.count("4️⃣") == 2 or currentDobbelstenen.count("5️⃣") == 2 or currentDobbelstenen.count("6️⃣") == 2) and (currentDobbelstenen.count("1️⃣") == 4 or currentDobbelstenen.count("2️⃣") == 4 or currentDobbelstenen.count("3️⃣") == 4 or currentDobbelstenen.count("4️⃣") == 4 or currentDobbelstenen.count("5️⃣") == 4 or currentDobbelstenen.count("6️⃣") == 4):
    print("Three of a kind is found!")