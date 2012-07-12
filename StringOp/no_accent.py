# -*-coding:Utf-8-*
import unicodedata
def no_accent(string):
    return unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore').decode('Utf-8')
