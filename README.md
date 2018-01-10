# rekrut
Zadanie rekrutacyjne.

Prerekwizyty:
Python (3.6), PIP, Django, Django REST Framework


```

pip install Django 

pip install djangorestframework
pip install markdown     
pip install django-filter
```

Uruchomienie:

```
cd rekrut
python manage.py runserver 8888

http://127.0.0.1:8888/messages/
```

API:
Pod adresem 
``` http://127.0.0.1:8888/messages-api/?recipient=aaa@bbb.pl ```
dostępne jest API udostępniające wszystkie (również już odczytane) wiadomości dla podanego w parametrze recipient adresu email
Dane logowania do api:
login: admin
hasło: haslohaslo