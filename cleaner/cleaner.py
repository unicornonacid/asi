#!/usr/bin/env python


import argparse
import polars as pl
from os import mkdir
from os import path
from sys import exit

parser = argparse.ArgumentParser(description='Czyszczenie pliku')
parser.add_argument('FROM', metavar='FROM', type=str, nargs=1,help='ścieżka do pliku do oczyszcenia')
parser.add_argument('TO', metavar='TO', type=str, nargs=1,help='ścieżka do pliku wynikowego')

args=parser.parse_args()
FROM=args.FROM[0]
TO=args.TO[0]

#Wczytanie pliku
df=pl.read_csv(FROM)

#policzenie rekordów
raw_number=df.select(pl.count())[0,0]

#zamiana stringów na int
client_converter={"Y":1, "N":0}
sex_converter={"M":1, "F":0}

df = df.with_columns(pl.col("Client").map_dict(client_converter))
df = df.with_columns(pl.col("Sex").map_dict(sex_converter))

#usunięcie rekordów z null/none
df = df.drop_nulls()

#tylko osoby w wieku poniżej 100 lat i powyżej 17 mogą kupować
df = df.filter(pl.col("Age")>17) 
df = df.filter(pl.col("Age")<100)

#policzenie rekordów po przetworzeniu
clean_number=df.select(pl.count())[0,0]

#sprawdzenie/utworzenie katalogów/plików
if not path.exists(path.dirname(TO)):
    mkdir(path.dirname(TO))

if path.exists(TO):
    print("Docelowy plik istnieje. Nie nadpisuję")
    exit(1)

#zapis pliku
df.write_csv(TO)

#raport końcowy
print(f"""Przetworzono {raw_number} rekordów.
Usunięto {raw_number-clean_number}.
Docelowy plik ma {clean_number} rekordów""")
    
