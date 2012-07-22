# -*-coding:Utf-8 -*
from Shell_functions import print_help
from StringOperation import StringOp
#Messages de départ !
print("==========CHALLENGE DU ZERO N°2===========")
print("Par Zérodazur !")
print("Utilisez la commande help pour voir les commandes !")

strop = StringOp()

while True:
    choice = input("$>")
    dict_func = {"help":"",
                 "starts": strop.starts_with,
                 "ends": strop.ends_with,
                 "inside": strop.word_inside
                 }
    dict_func["e"] = dict_func["ends"]
    if choice in dict_func.keys():
        arg = input("Chaîne à rechercher : ")
        list_words = dict_func[choice](arg)
    elif choice == "palindromes" or "palindrome":
        list_words = strop.palindromes()
    else: 
        print("Commande inconue !")
        continue
        
    for w in list_words: print(w)
    print("{} mots ont été trouvés.".format(len(list_words)))
    
    
