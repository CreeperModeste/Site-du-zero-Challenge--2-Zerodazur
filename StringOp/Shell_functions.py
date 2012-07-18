# -*-conding:Utf-8 -*
from StringOperation import *
strop = StringOp()


def print_words(list_words):
    print("{0} mots ont été trouvés :".format(len(list_words)))
    for word in list_words:
        print(word)
    
def help():
    print("Liste des commandes disponibles :")
    print("starts : affiche tous les mots \
commencant une chaîne.")
    print("ends : affiche tous les mots finnissant par une chaîne.")
    
def choix(operation):
    list_words = []
    to_search = input("Quel est la chaîne à chercher ?")
    if operation == "starts":
        list_words = strop.starts_with(to_search)
    elif operation == "ends":
        list_words = strop.ends_with(to_search)
    elif operation == "inside":
        list_words = strop.word_inside(to_search)
    elif operation == "croises":
        list_words = strop.mots_croises(to_search)
    print_words(list_words)   
    