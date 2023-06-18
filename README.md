# ASI

Aby uruchomić projekt należy wykonać polecenie:

```
./start_app.bash
```

## Architektura:

Aplikacja składa się z nastepujących komponentów:

1. Aplikacja do zarządzania  
   Wykorzystany jest biblioteka Streamlit.
   Aplikacja pozwala na:
   1. Wygenerowanie nowego zestawu danych i ich przygotowane (proces ETL)
   2. Wytrenowanie modelu 
   3. Sprawdzenie, czy występuje data drift
   4. Wypromowanie danego modelu na środowisko produkcyjne - aplikacja dla endusera
   
   Aplikacja jest dostępna pod adresem `localhost:8501`
   Cały backend oparty jest o Kedro. Aplikacja służy tylko uruchomienia odpowiednich procesów (pipelines) kedro.
2. Aplikacja do predykcji  
   dostępna pod adresem `localhost:4040`
   Po redeploymencie modelu konieczny jest restart kontenera
3. Preometheus  
   System do monitorowania systemu. Jest dostępny pod adesem `localhost:9090`
4. MLFlow 
   Dostępny pod adresem `localhost:5000`
5. Cadvisor  
   Aplikacja do monitorowania Dockera. Wystawia metryki dla Prometheusa
   
   
   

   
