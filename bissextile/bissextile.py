#! /usr/bin/python3.4
# -*-coding:Utf-8 -*

# @Author: Dahak Déborah <suika>
# @Date:   27-08-2019
# @Email:  dahak.deborah@gmail.com
# @Project: Python3
# @Filename: bissextile.py
# @Last modified by:   suika
# @Last modified time: 27-08-2019

annee = input("Saisissez une année : ")

try:
    annee = int(annee)
    assert annee > 0
except ValueError:
    print("Merci de saisir un nombre")
except AssertionError:
    print("Merci de saisir une année supérieure à 0.")
else:
    if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
        print(annee, "est une année bissextile.")
    else:
        print(annee, "n'est pas une année bissextile.")
