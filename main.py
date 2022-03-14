import random
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="dane"
)

nazwiska = []
imiona = []

wygenerowane = []


def PobierzDane(reg):
    with open(f"sources/{reg.lower()}_surnames.txt", "r", encoding="utf8") as file:
        for i in file:
            nazwiska.append(i.strip("\n").capitalize())

    with open(f"sources/{reg.lower()}_firstnames.txt", "r", encoding="utf8") as file:
        for i in file:
            imiona.append(i.strip("\n").capitalize())

def Generuj(n):
    for i in range(n):
        r = random.randint(0, len(imiona)-1)
        imie = imiona[r]
        r2 = random.randint(0, len(nazwiska)-1)
        nazwisko = nazwiska[r2]
        fullstring = imie + " " + nazwisko
        wygenerowane.append(fullstring)



y = int(input("Podaj ilość danych do wygenerowania: "))
reg = input("Podaj język (PL/EN)")

PobierzDane(reg)
Generuj(y)



with open("sources/wygenerowane.txt", "w", encoding="utf8") as zapisz:
    for i in wygenerowane:
        zapisz.write(i + "\n")



cursor = mydb.cursor()

val = []
with open("sources/wygenerowane.txt", "r", encoding="utf8") as odczyt:
    for i in odczyt:
        val.append(i.strip("\n").split())

command = "INSERT INTO info (imie, nazwisko) VALUES (%s, %s)"
cursor.executemany(command, val)

mydb.commit()

print(cursor.rowcount, "record inserted.")