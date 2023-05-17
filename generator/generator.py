#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Generowanie danych')
parser.add_argument('integers', metavar='X', type=int, nargs=1,help='liczba przypadków do wygenerowania')
args=parser.parse_args()
X=args.integers[0]

from mimesis import Generic
from mimesis.locales import Locale

from random import choices,sample,randrange

g = Generic(locale=Locale.EN)

fruits="""Apple
Aronia
Banana
Bearberry
Blackberry
Blackcurrant
Blueberry
Cantaloupe
Citron
Clementine
Coconut
Guava
Lime
Lychee
Mango
Orange
Peach
Plum
Quince
Raspberry
Redcurrant
Sambucus
Strawberries
""".splitlines()

# print(fruits)

#Zmienne

header=[]

header.append("Sex")
header.append("Age")
header.append(",".join(fruits))
header.append("Client")
print(",".join(header))

for z in range(X):

    output=[]

    # losowanie płci
    output.append(choices(["F","M"], weights=[0.4,0.6],k=1)[0])

    # wiek > 18 roku życia
    output.append(g.person.age(18))


    #czas reklam dla każdego owoca jest ustawiamy na 0
    fruits_dict={}
    for x in fruits:
        fruits_dict[x]=0;

    # losujemy listę owoców (od 1 do 7)
    for x in sample(fruits,k=randrange(8)):
        #dla każdego owocu losujemy czas reklam od 0 do 300
        fruits_dict[x]=randrange(300)

    # ustawiamy zmienne pomocnicze czy kupiła/kupił na 1
    Y=1
    N=1

    # Dla każdego owocu:
    for n,x in enumerate(fruits_dict):
        
        #Jeżeli nie oglądała to N wzrasta o 10
        if fruits_dict[x]==0:
            N=N+10
            #Jeżeli nie oglądała a indeks owocu jest parzysty, to N wzrasta o 5
            #dla nieparzystych obniża się o 5
            if n % 2 == 0:
                N=N+5
            else:
                N=N+20 
        else:
            #jeżeli oglądała reklamę owoców, to zmienna Y wzrasta o 10 + ile sekund oglądała reklamy podzielona przez 10
            Y=Y+fruits_dict[x]/9+10

    # wartość Y wzrasta również o wiek klienta
    Y=Y+output[1]

    #Dla klientek wartoś Y obniża się o 15
    if output[0]=='F':
        Y=Y-15

    # do zmiennej output dodawane są wartosci wygenerowanych reklam
    for x in sorted(fruits_dict.keys()):
        output.append(fruits_dict[x])

    # Najważniejsze: losowane jest czy klientka kupiła jakikolwiek sok. Losowanie jest proporcjonalne do wcześniej zdefiniowanych zmiennych Y i N
    output.append(choices(["Y","N"], weights=[Y,N],k=1)[0])

    # drukowane jest wynik, czy lista wszystkich zmiennych. Nie ma nagłówków.
    output=map(lambda x: str(x),output)
    print(",".join(output))


