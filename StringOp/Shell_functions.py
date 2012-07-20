# -*-conding:Utf-8 -*
from StringOperation import StringOp
strop = StringOp()


def print_words(list_words):
    print("{0} mots ont été trouvés :".format(len(list_words)))
    for word in list_words:
        print(word)
    
def print_help():
    print("Liste des commandes disponibles :")
    print("starts : affiche tous les mots \
commençant une chaîne.")
    print("ends : affiche tous les mots finnissant par une chaîne.")
    print("inside : affiche tous les contenant une chaîne.")
    print("croises : resolveur de mots croisés( remplacer les\
 lettres que vous ne savez pas par des astérisques. Ex : chat -> c**t)")
    
def choix(operation):
    list_words = []
    to_search = input("Quel est la chaîne à chercher ?")
    if to_search == "":
        print("Il faut écrire quelque chose pour que ça marche !")
        return
    if operation == "starts":
        list_words = strop.starts_with(to_search)
    elif operation == "ends":
        list_words = strop.ends_with(to_search)
    elif operation == "inside":
        list_words = strop.word_inside(to_search)
    elif operation == "croises":
        list_words = strop.mots_croises(to_search)
    elif operation == "correction":
        list_words = strop.correction(to_search)
    print_words(list_words)   
    