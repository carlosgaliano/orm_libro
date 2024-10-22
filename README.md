## Virtualenv

    virtualenv -p="C:\Python312\python.exe" .venv



**Como enlazar GIT y màs**



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

# Imprimiendo directamente con saltos de línea:

```python
mi_lista = ["Manzana", "Banana", "Naranja", "Pera"]
print(*mi_lista, sep='\n')
```

***

# modelo de pagina oficial

[QuerySet API reference | Django documentation | Django (djangoproject.com)](https://docs.djangoproject.com/en/5.0/ref/models/querysets/)

[Making queries | Django documentation | Django (djangoproject.com)](https://docs.djangoproject.com/en/5.0/topics/db/queries/#queryset-model-example)





***

# Enlaces

[Calculadora de Horas Trabajadas](https://www.calculator.io/es/calculadora-de-horas-trabajadas/)

[Funciones en Python](https://thedataschools.com/python/funciones/)

[Python Module Index](https://docs.python.org/3/py-modindex.html)

[Model field reference](https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-options)

[Djangogirls](https://tutorial.djangogirls.org/es/)

[Documentación de GitHub](https://docs.github.com/es)

[Framework Web Django (Python)](https://developer.mozilla.org/es/docs/Learn/Server-side/Django)

[Making queries](https://docs.djangoproject.com/en/5.0/topics/db/queries/)

[Models and databases](https://docs.djangoproject.com/en/5.0/topics/db/)

[Andrés Cruz](https://www.youtube.com/@desarrollolibre/playlists)

[¿Cuándo usar annotate y aggregate en Django? - DEV Community](https://dev.to/prox_sea/cuando-usar-annotate-y-aggregate-en-django-2gh4)

[Coffee bytes](https://coffeebytes.dev/es/)

[Django Tutorial - Python Tutorial - ingles](https://www.pythontutorial.net/django-tutorial/)

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

```python
for i in Modelo._meta.get_fields():
    print(i.name)
```

> ver la forma en SQL

```python
str(queryset.query)
```

****

# Django ORM

> llamado de modelos de la DB

```python
from django.contrib.auth.models import User
from blog.models import Blog, Author, Entry
users = User.objects.all()
blogs = Blog.objects.all()
authors = Author.objects.all()
entrys = Entry.objects.all()
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

```python
q1.union(q2)
```

> Cuando las 2 tablas **NO** tiene coincidencias entre los nombre de columnas se utiliza *_values\_list()* 

```python
User.objects.values_list("username", "email")
<QuerySet [('admin', 'galiano111@gmail.com'), ('yash', 'yashr@agiliq.com'), ('John', 'john@gmail.com'), ('Ricky', 'ricky@gmail.com'), ('sharukh', 'sharukh@hotmail.com'), ('Ritesh', 'ritesh@yahoo.com'), ('Billy', 'billy@gmail.com'), ('Radha', 'radha@gmail.com'), ('sohan', 'sohan@aol.com'), ('Raghu', 'raghu@rediffmail.com'), ('rishab', 'rishabh@yahoo.com')]>
```

> Como seleccionar campos en una consulta?

- Metodos *.values()* 

- .values_list()

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

```python
from django.contrib.auth.models import User
from blog.models import *
from django.db.models import Subquery

users = User.objects.all()
consulta = Author.objects.filter(id__in=Subquery(users.values('id')))
consulta.values()
<QuerySet [{'id': 1, 'name': 'carlos galiano', 'email': 'galiano111@gmail.com'}, {'id': 2, 'name': 'melissa Ferreira', 'email': 'melimelifer@gmail.com'}]>

# subconsulta invertida
autores = Author.objects.all()
consulta = User.objects.filter(id__in=Subquery(autores.values('id')))
print(*consulta.values(), sep="\n")
{'id': 1, 'password': 'pbkdf2_sha256$720000$1VleO7H4VLooUOgQbvvJYx$+s+DCBil8ReKYlaGj+JJfaexbg0MsAPXtJ90ApS41Vs=', 'last_login': datetime.datetime(2024, 3, 28, 21, 40, 52, 918854, tzinfo=datetime.timezone.utc), 'is_superuser': True, 'username': 'admin', 'first_name': 'Carlos', 'last_name': 'Galiano', 'email': 'galiano111@gmail.com', 'is_staff': True, 'is_active': True, 'date_joined': datetime.datetime(2024, 3, 12, 21, 21, 20, tzinfo=datetime.timezone.utc)}
{'id': 2, 'password': 'pbkdf2_sha256$720000$3YyBTemgUMmU24J6FMLTXi$ElAlVAchqJBllRqs8NbVmVmo6rhkJh5eW/1nQlMWVD8=', 'last_login': None, 'is_superuser': False, 'username': 'yash', 'first_name': 'Yash', 'last_name': 'Rastogi', 'email': 'yashr@agiliq.com', 'is_staff': False, 'is_active': True, 'date_joined': datetime.datetime(2024, 3, 12, 22, 35, 54, tzinfo=datetime.timezone.utc)}

str(consulta.values().query)
'SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."id" IN (SELECT U0."id" FROM "blog_author" U0)'
```

> Filtrar un conjunto de consultas con criterios basados en la comparacion de valores de campos

```python
# Now you can find the users wherefirst_name==last_name
from django.db.models import F
User.objects.filter(last_name=F("first_name")).values()
<QuerySet [{'id': 13, 'password': '', 'last_login': None, 'is_superuser': False, 'username': 'Guido', 'first_name': 'Guido', 'last_name': 'Guido', 'email': 'guido@example.com', 'is_staff': False, 'is_active': True, 'date_joined': datetime.datetime(2024, 3, 31, 6, 15, 12, 929214, tzinfo=datetime.timezone.utc)}]>

str(User.objects.filter(last_name=F("first_name")).values().query)
'SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" WHERE "auth_user"."last_name" = ("auth_user"."first_name")'

# con la misma letra de nombrer y apellido
print(*users.values("first_name", "last_name"), sep="\n")
...
{'first_name': 'Shabda', 'last_name': 'Raaj'}
{'first_name': 'Guido', 'last_name': 'Guido'}

# You can set the first letter from a string usingSubstr("first_name", 1, 1), so we do
User.objects.create(email="guido@example.com", username="Tim", first_name="Tim", last_name="Teters")
<User: Tim>
User.objects.sub()
```

> Como Filtar FileField sin ningun archivo?

```python
no_archivo = MyModel.objects.filter(
    Q(file='') | Q(file='None')
)
```

> Como realizar operaciones de union en Django OMR?

Una declaracion de Union SQL se utiliza para combinar datos o filas de dos o mas tablas en funcion de un campo comun entre ellos.  // Using select_related

```python
entry = Entry.objects.all().select_related("blog") #casino se utiliza
```

    {{ Entry.blog.name }} # y se puede obtener de esta forma

> Como encontrar el segundo registro más grande usando Django OMR?

```python
>>> print(*User._meta.get_fields(), sep="\n")
<ManyToOneRel: admin.logentry>
auth.User.id
auth.User.password
auth.User.last_login
auth.User.is_superuser
auth.User.username
auth.User.first_name
auth.User.last_name
auth.User.email
auth.User.is_staff
auth.User.is_active
auth.User.date_joined
auth.User.groups
auth.User.user_permissions
>>>
```

```python
>>> user = User.objects.order_by("-last_login")[1]
>>> user.first_name
'Yash'
>>> str(User.objects.order_by("-last_login").values().query)
'SELECT "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "auth_user" ORDER BY "auth_user"."last_login" DESC'
>>>
```

> Buscar filas que tengan valores de campos duplicados

```python
>>> from django.db.models import Count
>>> duplicados = User.objects.values('first_name').annotate(contar_nombre=Count('first_name')).filter(contar_nombre__gt=1)
>>> duplicados
<QuerySet [{'first_name': 'Sohan', 'contar_nombre': 2}, {'first_name': 'Tim', 'contar_nombre': 2}]>
>>>
```

# pagina 16...


