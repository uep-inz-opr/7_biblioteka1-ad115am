from collections import Counter
import sqlite3
if __name__ == "__main__":


    sqlite_con = sqlite3.connect(":memory:")
    cursor = sqlite_con.cursor()
    cursor.execute('''CREATE TABLE ksiazki (tytul data_type STRING, 
                          autor data_type STRING,  
                          rok data_type INTEGER
                          );''')
class Ksiazka():
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor
        #self.rok = rok
    ilosc = 0



liczba_ksiazek = int(input('podaj liczbe egzemplarzy: '))
lista_ksiazek = []
for i in range(liczba_ksiazek):
    egzemplarz = input('podaj tytul autora i rok: ')
    #nawiasy = (f'"{egzemplarz}"')
    tupla = eval(egzemplarz)
    lista_ksiazek.append(Ksiazka(tupla[0],tupla[1]))
    tytul_do_sql = tupla[0]
    print(tytul_do_sql)
    autor_do_sql = tupla[1]
    print(autor_do_sql)
    rok_do_sql = tupla[2]
    print(rok_do_sql)
    #query = f"INSERT INTO ksiazki (tytul,autor,rok) VALUES({tytul_do_sql},{autor_do_sql},{rok_do_sql})"
    query = f"INSERT INTO ksiazki(tytul,autor,rok) VALUES('Chatka puchatka','alan alexander',2005)"
    cursor.execute(query)
    #lista_ksiazek[i].ilosc+=1
    #lista_ksiazek.append(Ksiazka(tupla[0],tupla[1]))
    #lista_ksiazek[0].ilosc+=1
    #print(lista_ksiazek[i].tytul)
    #print(lista_ksiazek[i].ilosc)
query_select = f"select * from ksiazki"
cursor.execute(query_select)
result = cursor.fetchall()
print(result)
# for ksiazka in lista_ksiazek:
#     print(ksiazka.tytul,ksiazka.ilosc)
# print(lista_ksiazek.count("Chatka Puchatka"))






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
