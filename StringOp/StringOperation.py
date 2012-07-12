# -*-coding:Utf-8 -*
import re,time,unicodedata
from no_accent import no_accent
class StringOp:
    
    words = []
    def __init__(self):
        self.words = self.load_words()
        print(len(self.words))
        
    def load_words(self):
        with open("mots.txt",encoding="utf8") as fichier:
            str_words = fichier.read()
        fichier.close()
        return [line for line in str_words.split("\n")]
        
    def mots_croises(self):
        searched_word = input("Indiquez le mot à trouver :")
        upper_word = searched_word.upper()
        print(upper_word)
        exp_word = re.compile(upper_word.replace("*", "."))
        return [word  for word in self.words if re.match(exp_word,word) and len(word) == len(upper_word)]
    
    def starts_with(self,searched_word):
        print("Début de l'algo !")
        debut = time.time()
        searched_word = no_accent(searched_word).upper()
        match_words = []
        for word in self.words:
            i = 0
            if len(word) > len(searched_word):
                while i < len(searched_word):
                    if no_accent(word[i]) == searched_word[i]:
                        match = True
                    else: 
                        match = False
                        break
                    i += 1
                if match : match_words.append(word)   
        print("Durée de l'algo :",time.time() - debut,"seconde(s).") 
        return match_words
             
    def ends_with(self,searched_word):
        print("Début de l'algo !")
        debut = time.time()
        searched_word = no_accent(searched_word).upper()
        match_words = []
        for word in self.words:
            if len(word) > len(searched_word):
                y = 0
                i = len(word) - len(searched_word)
                match = False
                while y < len(searched_word):
                    if no_accent(word[i]) == searched_word[y]:
                        match = True
                    else: 
                        match = False
                        break
                    i += 1
                    y += 1
                if match : match_words.append(word)   
        print("Durée de l'algo :",time.time() - debut,"seconde(s).") 
        return match_words               
