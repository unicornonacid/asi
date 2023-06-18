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
   4. Wypromowanie danego modelu na środowisko produkcyjne - aplikacja dla endusera - promowanie oznacza, że trzeba zrestartować docker-compose
   
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
   
   

## Możliwy dalszy rozwój  

1. Migracja z Kedro do Airflow  
   Airflow zapewni bardziej stabilne środowisko pracy i możliwość wykonywania poszczególnych pipelinów warunkowo
2. Przeniesienie rejestru modeli z Kedro/MLFlow do zewnętrzego serwisu  
   Pozwoli lepiej wersjonować model
3. Przeniesienie aplikacji do chmury:
   1. Elastyczne skalowanie zasobów: AWS umożliwia dostosowanie zasobów obliczeniowych do wymagań naszego modelu. Można zwiększyć lub zmniejszyć moc obliczeniową w zależności od obciążenia - usługa AWS Auto Scaling
   2. Wykorzystanie usług zarządzanych: AWS oferuje usługi, które ułatwiają implementację i zarządzanie modelem uczenia maszynowego. Np Amazon SageMaker dostarcza platformę do tworzenia, trenowania i wdrażania modeli, a AWS Step Functions ułatwia tworzenie i zarządzanie workflow, dzięki temu ponosimy mniejsze koszty za pracę programistów, którzy korzystają a nie budują rozwiązanie od 0.
   3. Przechowywanie danych: AWS zapewnia usługę Amazon S3 (Simple Storage Service), gdzie można ustawić częstotliwość dostępu do danych, oznacza to, że im dostęp jest rzadszy tym koszt jest niższy.
   4. Wybór odpowiednich instancji w zależności od potrzeb. Jeżeli wiemy jakie będą potrzeby można skorzystać z rezerwacji lub opcji AWS Spot co znacząco wpływa na ostateczny rachunek.  

   
