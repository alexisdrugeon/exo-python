# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 9:22:59 2021

@author: Alexis Drugeon
"""

#Objectif : faire une fonction python qui additionne deux chiffres entrés en console

def addition_deux_chiffres():
    a = int(input("premier nombre a additionner : "))
    b = int(input("Second nombre a additionner : "))
    print("\n",a+b)
    return (a+b)

addition_deux_chiffres()