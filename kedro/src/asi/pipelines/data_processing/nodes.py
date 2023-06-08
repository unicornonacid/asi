import pandas as pd
from typing import Dict, List, Any


def generate_data(parameters: Dict) -> pd.DataFrame:
    """Generates data.

    Args:
        parameters: Configuration.
    Returns:
        Generated data.
    """
    from mimesis import Generic
    from mimesis.locales import Locale
    from random import choices, sample, randrange

    g = Generic(locale=Locale.EN)

    fruits = """Apple
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
    Strawberries""".splitlines()
    fruits = [fruit.strip() for fruit in fruits]

    # Zmienne
    headers = ["Sex", "Age"]
    headers.extend(fruits)
    headers.append("Client")

    data = pd.DataFrame(columns=headers)

    for z in range(parameters["data_size"]):
        # losoanie płci
        # wiek > 18 roku życia
        row: list[str | int] = [choices(["F", "M"], weights=[0.4, 0.6], k=1)[0], g.person.age(18)]

        # czas reklam dla każdego owoca jest ustawiamy na 0
        fruits_dict = {}
        for x in fruits:
            fruits_dict[x] = 0
        # losujemy listę owoców (od 1 do 7)
        for x in sample(fruits, k=randrange(8)):
            # dla każdego owocu losujemy czas reklam od 0 do 300
            fruits_dict[x] = randrange(300)
        # ustawiamy zmienne pomocnicze czy kupiła/kupił na 1
        Y = 1
        N = 1
        # Dla każdego owocu:
        for n, x in enumerate(fruits_dict):
            # Jeżeli nie oglądała to N wzrasta o 10
            if fruits_dict[x] == 0:
                N = N + 10
                # Jeżeli nie oglądała a indeks owocu jest parzysty, to N wzrasta o 5
                # dla nieparzystych obniża się o 5
                if n % 2 == 0:
                    N = N + 5
                else:
                    N = N + 20
            else:
                # jeżeli oglądała reklamę owoców, to zmienna Y wzrasta o 10 + ile sekund oglądała reklamy podzielona przez 10
                Y = Y + fruits_dict[x] / 9 + 10

        # wartość Y wzrasta również o wiek klienta
        Y = Y + row[1]

        # Dla klientek wartoś Y obniża się o 15
        if row[0] == 'F':
            Y = Y - 15

        # do zmiennej output dodawane są wartosci wygenerowanych reklam
        for x in sorted(fruits_dict.keys()):
            row.append(fruits_dict[x])

        # Najważniejsze: losowane jest czy klientka kupiła jakikolwiek sok. Losowanie jest proporcjonalne do wcześniej zdefiniowanych zmiennych Y i N
        row.append(choices(["Y", "N"], weights=[Y, N], k=1)[0])

        # drukowane jest wynik, czy lista wszystkich zmiennych. Nie ma nagłówków.
        data.loc[len(data.index)] = row

    return data


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """Cleans data and returnes clean data.

    Args:
        data: Generated data.
    Returns:
        Clean data.
    """
    # policzenie rekordów
    row_number = len(data.index)

    # zamiana stringów na int
    client_converter = {"Y": 1, "N": 0}
    sex_converter = {"M": 1, "F": 0}

    data["Client"] = data["Client"].map(client_converter)
    data["Sex"] = data["Sex"].map(sex_converter)

    # usunięcie rekordów z null/none
    data = data.dropna()

    # tylko osoby w wieku poniżej 100 lat i powyżej 17 mogą kupować
    data = data.query('Age > 17 and Age < 100')

    # policzenie rekordów po przetworzeniu
    clean_number = len(data.index)

    # raport końcowy
    print(f"""Przetworzono {row_number} rekordów.
    Usunięto {row_number - clean_number}.
    Docelowy plik ma {clean_number} rekordów""")

    return data
