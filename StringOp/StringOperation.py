# -*-coding:Utf-8 -*
import re,time,unicodedata
class StringOp:
    
    words = []
    def __init__(self):
        self.words = self.load_words()
        print("Il y a {0} mots dans le dico.".format(len(self.words)))
        
    def load_words(self):
        time_ = time.time()
        with open("mots.txt",encoding="utf8") as fichier:
            str_words = fichier.read()
        fichier.close()
        print("Durée de lecture du fichier :",time.time() - time_)
        return [line for line in str_words.split("\n")]
    
    def no_accent(self, string):
        return unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore').decode('Utf-8')
        
    def mots_croises(self,searched_word):
        upper_word = self.no_accent(searched_word).upper()
        print(upper_word)
        exp_word = re.compile(upper_word.replace("*", "."))
        return [word  for word in self.words if re.match(exp_word,word) and len(word) == len(upper_word)]
    
    def starts_with(self,searched_word):
        print("Début de l'algo !")
        debut = time.time()
        searched_word = self.no_accent(searched_word).upper()
        match_words = []
        for word in self.words:
            i = 0
            if len(word) > len(searched_word):
                while i < len(searched_word):
                    if self.no_accent(word[i]) == searched_word[i]:
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
        searched_word = self.no_accent(searched_word).upper()
        match_words = []
        for word in self.words:
            if len(word) > len(searched_word):
                y = 0
                i = len(word) - len(searched_word)
                match = False
                while y < len(searched_word):
                    if self.no_accent(word[i]) == searched_word[y]:
                        match = True
                    else: 
                        match = False
                        break
                    i += 1
                    y += 1
                if match : match_words.append(word)   
        print("Durée de l'algo :",time.time() - debut,"seconde(s).") 
        return match_words        
           
    def word_inside(self,searched_word):
        upper_word = self.no_accent(searched_word).upper()
        rex_word = re.compile(".{1,}" + upper_word +".{1,}")
        return [word  for word in self.words if re.match(rex_word,word)]
    
    def palindromes(self):
        match_word = []
        for w in self.words:
            iw = w[::-1] 
            if iw == w: match_word.append(w)
        return match_word
            