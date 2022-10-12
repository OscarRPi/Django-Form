# Formulario CRUD con Django y Sqlite 

Este proyecto esta hecho con el Framework Django, estructurando una api CRUD monolitica que guarda los datos en una base de datos sqlite

Back: Python (Django)
Front: HTML,CSS(Bootstrap)
Unit-tests: django.test, selenium

Sistemas operativos usados:

*Windows 10 Pro
*Linux Debian 11

Python version: 3.10.7

# Introduccion

Este tutorial esta dividido en cuatro secciones:

1. Creando un entorno virtual

1.1 Instalando requerimientos
1.2 Iniciar el servidor

2. Correr unit-test para la app
3. Correr unit-test funcionales

4. Probar aplicacion en la nube

4.1 Mejoras (En construccion) 

## 1. Creando un entorno virtual

Primero debemos asegurarnos de tener instalado Python y Git. 

En Linux, debemos instalar python3-venv despues de tener Python3

En una consola de Debian corremos lo siguiente:

```cmd
sudo apt install python3-venv
```
En una consola de windows ('cmd.exe') o Linux (konsole), correr el siguiente comando:

* Crear un entorno virtual en el directorio actual llamado 'myvenv'
```cmd
python -m venv myvenv
```
* Activar el entorno virtual que esta ubicado en myvenv/

- Linux
```cmd
source myvenv/bin/activate
```
- Windows
```cmd
myvenv\Scripts\activate
```
* Actualizar pip (Linux y Windows)
```cmd
python -m pip install --upgrade pip
```
* Clonar este repositorio (Linux y Windows)
```cmd
git clone https://github.com/OscarRPi/Django-Form.git
```

```cmd
cd Django-Form
```

### 1.1 Instalando requerimientos (Linux y Windows)

```cmd
pip install -r requirements.txt
```

### 1.2 Iniciar el servidor (Linux y Windows)

```cmd
python manage.py runserver
```
En la consola aparecera la direccion y el puerto que debemos abrir (http://127.0.0.0.1:8000)

Copiar esta direccion y en un navegador buscar esta url

## 2. Correr unit-test para la app

En la consola de Windows/Linux detener el servidor con 'ctrl + C' y ejecutar el siguiente comando:

```cmd
python manage.py test formapp
```
Esto ejecutará 14 unit-tests para: 

* urls.py
* views.py
* models.py
* forms.py

## 3.  Correr unit-test funcionales

> (Windows) Se recomienta usar Google Chrome Versión 106.0.5249.103 
> (Linux)   Se recomienta usar Chromium Version 106.0.5249.91 

En la consola de Windows/Linux detener el servidor con 'ctrl + C' y ejecutar el siguiente comando:

```cmd
python manage.py test functional_tests
```

Esto ejecutara 4 unit-tests que simulan el comportamiento del usuario en la pagina

## 4.  Probar aplicacion en la nube

Se ha desplegado en la nube a traves de la pagina pythonanywhere.com

[Django_Form](https://djangotesting.pythonanywhere.com/)

## 4.1.  Mejoras (en construccion)

[Django_Form_REST](https://github.com/OscarRPi/Django-Form-REST)
