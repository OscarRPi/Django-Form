# Formulario CRUD con Django y Sqlite 

Este proyecto esta hecho con el Framework Django, estructurando una api CRUD monolitica que guarda los datos en una base de datos sqlite

Back: Python (Django)
Front: HTML,CSS(Bootstrap)
Unit-tests: django.test, selenium

# Introduccion

Este tutorial esta dividido en tres secciones:

1. Creando un entorno virtual
1.1 Instalando requerimientos
1.2 Iniciar el servidor

2. Correr unit-test para la app
3. Correr unit-test funcionales

## 1. Creando un entorno virtual

Primero debemos asegurarnos de tener instalado Python y Git. 
La version de Python que se uso para hacer este proyecto es: 3.10.7  

En una consola de windows ('cmd.exe') correr el siguiente comando:

* Crear un entorno virtual en el directorio actual llamado 'myvenv'
```cmd
python -m venv myvenv
```
* Activar el entorno virtual que esta ubicado en myvenv/
```cmd
myvenv\Scripts\activate
```
* Actualizar pip
```cmd
python -m pip install --upgrade pip
```
* Clonar este repositorio
```cmd
git clone https://github.com/OscarRPi/Django-Form.git
```

### 1.1 Instalando requerimientos

```cmd
pip install -r requirements.txt
```

### 1.2 Iniciar el servidor

Cambiar a la ruta donde esta ubicado el archivo manage.py

```cmd
cd Django-Form
```

```cmd
python manage.py runserver
```

En la consola de Windows aparecera la direccion y el puerto que debemos abrir (http://127.0.0.0.1:8000)

Copiar esta direccion y en un navegador buscar esta url

> Se recomienta usar Google Chrome Versión 106.0.5249.103 para poder correr la seccion 3 de este tutorial

## 2. Correr unit-test para la app

En la consola de Windows detener el servidor con 'ctrl + C' y ejecutar el siguiente comando:

```cmd
python manage.py test formapp
```
Esto ejecutará unit-tests para urls.py / views.py / models.py / forms.py

## 3.  Correr unit-test funcionales

En la consola de Windows detener el servidor con 'ctrl + C' y ejecutar el siguiente comando:

```cmd
python manage.py test functional_tests
```

Esto ejecutara unit-tests que simulan el comportamiento del usuario en la pagina