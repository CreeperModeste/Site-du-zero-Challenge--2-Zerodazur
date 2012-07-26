# -*-conding:Utf-8 -*
from StringOperation import StringOp


def print_words(list_words):
    print("{0} mots ont été trouvés :".format(len(list_words)))
    for word in list_words:
        print(word)
    
def print_help():
    print("Liste des commandes disponibles :")
    print("starts (ou s): affiche tous les mots \
commençant une chaîne.")
    print("ends (ou e): affiche tous les mots finnissant par une chaîne.")
    print("inside (ou i): affiche tous les contenant une chaîne.")
    print("croises (ou cr): resolveur de mots croisés(remplacer les\
 lettres que vous ne savez pas par des astérisques. Ex : chat -> c**t).")
    print("palindromes (ou p): cherche tous les palindrome du dictionnaire.")
    print("correction (ou c): rentrez un mot et il revoie tous les mots correspondant avec\
 une fautes de frape.")
    

    