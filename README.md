**Como enlazar GIT**



***…or create a new repository on the command line***



1. echo "# orm_libro" >> README.md

2. git init

3. git add README.md

4. git commit -m "first commit"

5. git branch -M main

6. git remote add origin https://github.com/carlosgaliano/orm_libro.git

7. git push -u origin main
   
   

***…or push an existing repository from the command line***



1. git remote add origin https://github.com/carlosgaliano/orm_libro.git

2. git branch -M main

3. git push -u origin main

***

# Enlaces

[Funciones en Python](https://thedataschools.com/python/funciones/)

***

# OMR Django

> Limpiar shell de pythom

```python
import os
os.system("cls")
```

> Para cargar un modelo

```python
 from django.contrib.auth.models import User
```

> Para cargar su contenido según su \__str__()

```python
users = User.objects.all()
```

> para saber el nombre de las columnas de la tabla DB

```python
campos = User._meta.get_fields()
campos
```

> Como hacer consultas en Django ORM

- queryset_1 | queryset_2

- .filter( Q (<condicion 1>) | Q (<condicion 2>) // se debe importar __from django.db.models import Q__

```python
users.filter(first_name__startswith='R') | users.filter(last_name__startswith='U')
```

```python
 from django.db.models import Q
 users.filter(Q(first_name__startswith='R')|Q(last_name__startswith='U'))
```

```sql
SELECT username, first_name, last_name, email FROM auth_user WHERE first_name like 'R%' OR last_name like 'U%'
```

> Como hacer consultas con AND en Django ORM

- .filter(<conicion 1>, <conicion 2>)

- queryset_1 & queryset_2

- .filter(Q(<conicion 1>) & Q(<conicion 1>))

```python
User.objects.filter(first_name__startswith='R', last_name__startswith='D')
```

```python
User.objects.filter(first_name__startswith='R') & User.objects.filter(last_name__startswith='D')
```

```python
from django.db.models import Q
User.objects.filter(Q(first_name__startswith='R') & Q(last_name__startswith='D'))
```

```sql
SELECT username, first_name, last_name, email FROM auth_user WHERE first_name like 'R%' AND last_name like 'D%'
```

> Como hacer una consulta __NOT__ en Django ORM

- .exclude(<condition>)

- .filter(~Q(<condition>))

```python
User.objects.exclude(id__lt=5)
```

```python
User.objects.filter(~Q(id__lt=5))
```

```sql
SELECT username, first_name, last_name, email FROM auth_user WHERE NOT id < 5
```

> Como hacer una union entre 2 consultas iguales o diferentes en Django ORM


