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

> ver la forma en SQL

```python
str(queryset.query)
```

****

# Django ORM

 

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

```python
q1.union(q2)
```

> Cuando las 2 tablas **NO** tiene coincidencias entre los nombre de columnas se utiliza *_values\_list()* 

```python
User.objects.values_list("username", "email")
<QuerySet [('admin', 'galiano111@gmail.com'), ('yash', 'yashr@agiliq.com'), ('John', 'john@gmail.com'), ('Ricky', 'ricky@gmail.com'), ('sharukh', 'sharukh@hotmail.com'), ('Ritesh', 'ritesh@yahoo.com'), ('Billy', 'billy@gmail.com'), ('Radha', 'radha@gmail.com'), ('sohan', 'sohan@aol.com'), ('Raghu', 'raghu@rediffmail.com'), ('rishab', 'rishabh@yahoo.com')]>
```

> Como seleccionar campos en una consulta?

- Metodos *.values()* y *.values_list()*

- Metodo *.only("nomber de la columna", "nomber de la columna")*  _devuelve un diccionario_

```python
User.objects.filter(first_name__startswith="R").values('username', 'email')
<QuerySet [{'username': 'Ricky', 'email': 'ricky@gmail.com'}, {'username': 'Ritesh', 'email': 'ritesh@yahoo.com'}, {'username': 'Radha', 'email': 'radha@gmail.com'}, {'username': 'Raghu', 'email': 'raghu@rediffmail.com'}, {'username': 'rishab', 'email': 'rishabh@yahoo.com'}]>
'SELECT "auth_user"."username", "auth_user"."email" FROM "auth_user" WHERE "auth_user"."first_name" LIKE R% ESCAPE \'\\\''

User.objects.filter(first_name__startswith="R").values_list('username', 'email')
<QuerySet [('Ricky', 'ricky@gmail.com'), ('Ritesh', 'ritesh@yahoo.com'), ('Radha', 'radha@gmail.com'), ('Raghu', 'raghu@rediffmail.com'), ('rishab', 'rishabh@yahoo.com')]>
'SELECT "auth_user"."username", "auth_user"."email" FROM "auth_user" WHERE "auth_user"."first_name" LIKE R% ESCAPE \'\\\''
```

```python
User.objects.filter(first_name__startswith="R").only('username', 'email')
<QuerySet [<User: Ricky>, <User: Ritesh>, <User: Radha>, <User: Raghu>, <User: rishab>]>
str(User.objects.filter(first_name__startswith="R").only('username', 'email').query)
'SELECT "auth_user"."id", "auth_user"."username", "auth_user"."email" FROM "auth_user" WHERE "auth_user"."first_name" LIKE R% ESCAPE \'\\\''sql
```

> Como hacer una expresión de subconsulta en Django?


