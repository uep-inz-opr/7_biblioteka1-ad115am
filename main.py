from collections import Counter

class Ksiazka():
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor
        #self.rok = rok
    ilosc = 0



#liczba_ksiazek = int(input())
lista_ksiazek = []
egzemplarz = input()
tupla = eval(egzemplarz)
lista_ksiazek.append(Ksiazka(tupla[0],tupla[1]))
lista_ksiazek[0].ilosc+=1
lista_ksiazek.append(Ksiazka(tupla[0],tupla[1]))
lista_ksiazek[0].ilosc+=1
print(lista_ksiazek[0].tytul)
print(lista_ksiazek[0].ilosc)






# tytuly = []
# tytuly.append(lista_ksiazek[0].tytul)
# tytuly.append(lista_ksiazek[1].tytul)
# print(tytuly)
# counter = Counter(tytuly)
# counter_dict=(dict(counter))
# print(counter_dict)
# counter_tuple = tuple(counter_dict)
# print(counter_tuple)
#
# # print(type(counter))
# lista_z_ilosciami_egzemplarzy = []
#lista_ksiazek.append(tupla())
# print(tupla)
# print(type(tupla))
# lista_ksiazek.append(tupla)
# lista_ksiazek.append(tupla)
# slownik = {'tytul':[],'ilosc':0}
# slownik['tytul'].append(tupla[0])
# slownik['ilosc']+=1;
# print(slownik)
# print(lista_ksiazek)
# tytuly=[]
# tytuly.append(tupla[0])
# tytuly.append(tupla[0])
# print(f'tytuly: {tytuly}')
# counter = Counter(tytuly)
# print(dict(counter))
# print(type(counter))
# a= '(" Chatka Puchatka ", " Alan Alexander Milne ", 2014)'
# b = ast.literal_eval()(a)
# print(type(b))
