
# do zrobienia
[ ] zaprojektowanie workflowu przepływu danych, modeli
[ ] wybranie aplikacji do zarządzania/schedulowania - mage za bardzo skomplikowany
[ ] sparametryzowanie generatora danych (by robił data drift)
[ ] skrypt ETL
[ ] stworzenie aplikacji do trenowania modelu
[ ] aplikacja do konsumowania modelu
    [ ] frontend
    [ ] backend
[ ] aplikacja do sprawdzania data driftu
[ ] dokeryzacja wszystkiego
[ ] dokumentacja

# proponowany workflow

1. Generowanie danych
2. Dane zapisane w repozytorium danych (może być katalog)
3. uruchomienie ETL ( raw -> cleaned)
4. trenowanie modelu ( cleaned -> model_repo)
5. ustalenie hiperparametrów ????
6. deployment aplikacji (model_repo -> app)
7. sprawdzenie data drift 
   1. Generowanie nowych danych
   2. ETL
   3. porównanie danych z poprzednim
   4. jeżeli jest drift -> redeployment nowego modelu
   5. 