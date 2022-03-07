import random
# Random gets inported here.

import sys, os
# System gets inported here.

import time
# Time gets imported here.

from collections import Counter

os.system('cls')
# The console gets cleared.

print("------------------------------------------------------------------------------------------")
print(" ")
print("Hello, welcome to Yahtzee.")
print("The goal is to have score the highest score possible, by havinbg certain paterns or orders with your dices.")
print("When you trow the dices you can choose to keep or shuffle certain dices for higher scores.")
print("you have three try's to get the highest score possible.")
print("(Made by: Niels van Rheenen, V4D, Het Streek Lyceum.)")
print(" ")
print("------------------------------------------------------------------------------------------")
print(" ")
# Printing the explaination and rules of the game.

time.sleep(0)
# Wating five seconds.

os.system('cls')
# Clearing the console

dices = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
# Making a list with all the dices.

rnd1 = random.choice(dices)
rnd2 = random.choice(dices)
rnd3 = random.choice(dices)
rnd4 = random.choice(dices)
rnd5 = random.choice(dices)

currentDices = [rnd1, rnd2, rnd3, rnd4, rnd5]
# Picking random dices from the list and putting the five random dices in a new list.

print("------------------------------------------------------------------------------------------")
print("These are your dices:")
print(currentDices)
print("------------------------------------------------------------------------------------------")
print(" ")
# Printing the random dices.

hold = input("Do you want to keep your dices. ")
# Asking if the user wants to keep their dices.

turn = 0

while hold == "no":
    print(" ")
    print("Continuing")
    print(" ")

    # While hold equals 0

    change1 = input("Do you want to change dice 1 ('yes' or 'no')? ")
    change2 = input("Do you want to change dice 2 ('yes' or 'no')? ")
    change3 = input("Do you want to change dice 3 ('yes' or 'no')? ")
    change4 = input("Do you want to change dice 4 ('yes' or 'no')? ")
    change5 = input("Do you want to change dice 5 ('yes' or 'no')? ")
    # Asking if the user wich dices they want to change or keep.

    if change1 == "yes":
        currentDices[0] = random.choice(dices)
    if change2 == "yes":
        currentDices[1] = random.choice(dices)
    if change3 == "yes":
        currentDices[2] = random.choice(dices)
    if change4 == "yes":
        currentDices[3] = random.choice(dices)
    if change5 == "yes":
        currentDices[4] = random.choice(dices)
    # Changing the dices.

    print(" ")
    print("------------------------------------------------------------------------------------------")
    print("These are your new dices:")
    print(currentDices)
    print("------------------------------------------------------------------------------------------")
    print(" ")
    # Printing the new dices.

    turn = turn + 1

    if turn == 2:
        hold = "yes"
    else:
        hold = input("Do you want to keep these dices ('yes' or 'no')? ")
    # Checking the amount of times the user has changed their dices exeeds 3.

    print(" ")
    print("------------------------------------------------------------------------------------------")
    print("These are your final dices")
    print(currentDices)
    print("------------------------------------------------------------------------------------------")
    print(" ")
    # Printing the final dices.


if currentDices.count('1️⃣') == 3 or currentDices.count('2️⃣') == 3 or currentDices.count('3️⃣') == 3 or currentDices.count('4️⃣') == 3 or currentDices.count('5️⃣') == 3 or currentDices.count('6️⃣') == 3:
    threeOfAKind = True
    print("three of a kind")
else: threeOfAKind = False
# Checking for three of a kind

if currentDices.count("1️⃣") == 4 or currentDices.count("2️⃣") == 4 or currentDices.count("3️⃣") == 4 or currentDices.count("4️⃣") == 4 or currentDices.count("5️⃣") == 4 or currentDices.count("6️⃣") == 4:
    fourOfAKind = True
    print("four of a kind")
else: fourOfAKind = False
# Checking for four of a kind

if currentDices.count("1️⃣") == 5 or currentDices.count("2️⃣") == 5 or currentDices.count("3️⃣") == 5 or currentDices.count("4️⃣") == 5 or currentDices.count("5️⃣") == 5 or currentDices.count("6️⃣") == 5:
    Yahtzee = True
    print("yahtzee")
else: Yahtzee = False
# Checking for yahtzee

if ('1️⃣' and '2️⃣' and '3️⃣' and '4️⃣') or ('2️⃣' and '3️⃣' and '4️⃣' and '5️⃣') or ('3️⃣' or'4️⃣' and '5️⃣' and '6️⃣') in currentDices:
    smallStreet = True
    print("small street")
else: smallStreet = False
# Checking for small street

bigStreetList1 = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣']
bigStreetList2 = ['2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣']

if bigStreetList1 == currentDices or bigStreetList2 == currentDices:
    bigStreet = True
    print("big street")
else: bigStreet = False
# Checking for big street

if (currentDices.count("1️⃣") == 2 or currentDices.count("2️⃣") == 2 or currentDices.count("3️⃣") == 2 or currentDices.count("4️⃣") == 2 or currentDices.count("5️⃣") == 2 or currentDices.count("6️⃣") == 2) and (currentDices.count("1️⃣") == 3 or currentDices.count("2️⃣") == 3 or currentDices.count("3️⃣") ==3 or currentDices.count("4️⃣") == 3 or currentDices.count("5️⃣") == 3 or currentDices.count("6️⃣") == 3):
    fullHouse = True
    print("full house")
else: fullHouse = False
# Checking for full house


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
# Printing all of the results if they are found.