# -*-coding:Utf-8 -*
#Fichier de test !
from StringOperation import StringOp
s = StringOp()
i = 0
l = []
print(s.lev("chie","chien"))
for w in s.words:
    i += 1
    print(w)
    print(i)
    if s.lev(w,"chie".upper()) == 1:
        l.append(w)
for i in l:
    print(i)
input()
