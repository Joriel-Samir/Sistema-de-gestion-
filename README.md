# Sistema de Gestión de Ingresos y Gastos

Aplicación web desarrollada con **Django** para la gestión de ingresos y gastos personales por usuario.  
Permite registrar, visualizar, editar y eliminar movimientos financieros, mostrando totales automáticos.

---

## Funcionalidades

- Registro de ingresos y gastos
- Descripción y fecha del gasto
- Cálculo automático de:
  - Total de ingresos
  - Total de gastos
  - Dinero restante
- CRUD completo (Crear, Leer, Editar, Eliminar)
- Autenticación de usuarios
- Interfaz responsive con **Bootstrap 5**
- Protección CSRF integrada

---

## Tecnologías usadas

- Python 3.12  
- Django 5.2.6  
- Bootstrap 5  
- HTML5  
- SQLite 

  --- Estructura del proyecto
Sistema_Gestion/
│
├── Sistema_Gestion/
│ ├── settings.py
│ ├── urls.py
│ └── views.py
│
├── templates/
│ ├── base.html
│ ├── gestion.html
│ └── añadir_datos.html
│
├── manage.py
└── requirements.txt

## Instalación y configuración

### Clonar el repositorio

```bash
https://github.com/Joriel-Samir/Sistema-de-gestion-.git
```
###Configura tu entorno virtual 
-Windows
python -m venv venv
venv\Scripts\activate

-Linux/MacOs
python3 -m venv venv
source venv/bin/activate

###Instala las librerias 

pip install -r requirements.txt

###Realiza las migraciones
python manage.py makemigrations
python manage.py migrate

####Create un super usuario para administrar las tablas
python manage.py createsuperuser




