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

    ilosc = 0

liczba_ksiazek = int(input('podaj liczbe egzemplarzy: '))
lista_ksiazek = []
for i in range(liczba_ksiazek):
    egzemplarz = input('podaj tytul autora i rok: ')
    tupla = eval(egzemplarz)
    lista_ksiazek.append(Ksiazka(tupla[0],tupla[1]))
    tytul_do_sql = tupla[0]
    autor_do_sql = tupla[1]
    rok_do_sql = tupla[2]
    query = f"INSERT INTO ksiazki(tytul,autor,rok) VALUES('{tytul_do_sql}','{autor_do_sql}',{rok_do_sql})"
    cursor.execute(query)


query_count = f"select tytul, autor, count(tytul) from ksiazki group by tytul order by tytul"
cursor.execute(query_count)
result_count = cursor.fetchall()
for row in result_count:
    print(row)







