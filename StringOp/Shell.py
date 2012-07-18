# -*-coding:Utf-8 -*
from Shell_functions import *
#Messages de départ !
print("==========CHALLENGE DU ZERO N°2===========")
print("Par Zérodazur !")
print("Utilisez la commande help pour voir les commandes !")



while True:
    choice = input("$>")
    if choice == "help" or choix == "h": help()
    elif choice == "starts": choix("starts")
    elif choice == "ends": choix("ends")
    elif choice == "inside": choix("inside")
    elif choice == "croises": choix("croises")