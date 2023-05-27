# Predykcja zakupów soków firmy PolJuice

## Opis biznesowy
Firma PoJuice zajmuje się sprzedażą w swoim sklepie internetowym soków z różnych owoców. Oto lista wszystkich rodzajów soków:

- Apple
- Aronia
- Banana
- Bearberry
- Blackberry
- Blackcurrant
- Blueberry
- Cantaloupe
- Citron
- Clementine
- Coconut
- Guava
- Lime
- Lychee
- Mango
- Orange
- Peach
- Plum
- Quince
- Raspberry
- Redcurrant
- Sambucus
- Strawberries

Firma prowadzi szeroko zakrojoną akcję promocyjną, na którą składa się przede wszystkim reklamy wideo, publikowane w internecie. Każda reklama dotyczy tylko jednego smaku soków. Dzięki doskonałej platformie analitycznej, firma jest w stanie określić ile minut każdej reklamy oglądała każda osoba, która weszła na stronę sklepu internetowego firmy. System analityczny pozwala również określić płeć osoby, wiek (w latach). Po każdej wizycie dodawana jest informacja, czy osoba kupiła sok, czy nie.
Oto przykładowe rekordy danych z systemu analitycznego:

```
M,22,0,30,65,0,0,0,0,0,0,0,183,0,0,0,0,0,0,0,0,0,166,47,264,N
M,30,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Y
M,36,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,116,0,0,0,0,0,0,0,N
F,41,0,0,0,76,0,0,0,0,0,0,0,9,0,0,0,298,0,0,0,0,0,120,0,Y
M,35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,N
M,35,0,210,0,114,0,287,0,0,191,0,0,0,0,0,0,0,0,0,0,0,0,0,0,N
M,33,0,225,0,7,229,0,0,0,0,0,0,294,0,0,0,0,153,0,0,296,53,0,0,Y
F,57,0,0,0,0,219,0,0,0,142,201,0,0,0,0,0,0,0,0,0,0,0,0,299,N
```

1. kolumna: Płeć (M/F)
2. komuna: wiek w latach (użytkownicy mają od 18 do 100 lat)
3. kolumna do 28.: liczba sekund ile reklama danego soku była widziana przez użytkownia.
29. Czy użytkownik dokonał zakupu (Y/N)

## Aplikacja analityczna
Zadaniem zespołu było stworzenie aplikacji dla działu marketingu, która na podstawie wprowadzonych danych (kolumny od 1. do 28.), przewidzą czy klient dokonał zakupu. Aplikacja ma mieć interface webowy.

## Architektura
### Model
Jako model została wybrana regresja logistyczna w implementacji `LogisticRegression` z pakietu `scikit`.
### Architektura właściwa
Jeżeli nie zostało opisane inaczej, cały pipeline opiera się o system **Kedro**, odpalony w **Dockerze**.
#### Generowanie danych
	Dane są pobierane z zewnętrzengo systemu za pomocą dostarczonego skryptu
#### Zapisanie danych w repozytorium
	Dane są zapisywane w zewnętznym repozytorium opartym o **DVC**
#### ETL
	Dane są przekodowywane (**polars**) i sprawdzana jest ich poprawność (**Great Expectations**), następne zapisywane w repozytorium **DVC**
#### Trening
	Model jest trenowany razem z doborem hiperparametrów za pomocą wbudowanych w bibliotekę scilearn procedurę `GridSearchCV`. Trening jest monitorowany za pomocą narzędzia `MLflow`. Wytrenowany model zapisywany jest do rejestru modeli udostępnionego przez `DVC`
#### Operacjonalizacja
	Wytrenowany model słuzy jako podstawa do stworzenia obrazu Dokerowego aplikacji webowej opartej o `Streamlit`, Aplikacja jest deployowana w tym samym miejscu co **Kedro**
#### Data drift
	Zmiana danych jest moniotorwana za pomocą biblioteki `Frouros` Jeżeli zmiany zostaną wykryte, następuję ponowne wytrenowanie modelu i jego deployment
#### Monitoring środowiska
	Monitoring środowiska jest oparty o system do zbierania metryk Prometheus
	