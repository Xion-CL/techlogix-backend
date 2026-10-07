# 📦 TechLogix S.A. - Sistema Backend Django

**Evaluación Sumativa 02 - Backend**  
**Área:** Informática - Analista Programador  
**Docente:** Paulo Simunovic Oyarzun  
**Fecha:** Octubre 2026

## 🎯 Descripción del Proyecto

Sistema web Back End desarrollado en **Django** con base de datos **PostgreSQL** para la gestión del catálogo e inventario de productos de la distribuidora TechLogix S.A.

## ✅ Características Implementadas

- ✅ Conexión a PostgreSQL con variables de entorno (`.env`)
- ✅ Modelos `Categoria` y `Producto` con FK
- ✅ Panel de administración nativo personalizado (`list_display`, `list_filter`, `search_fields`)
- ✅ CRUD completo (Crear, Leer, Actualizar, Eliminar)
- ✅ Sistema de autenticación con Login personalizado
- ✅ Control de acceso por roles: **Administrador** (C-R-U-D) y **Asistente** (solo R)
- ✅ Protección CSRF en todos los formularios
- ✅ Mixins personalizados para permisos
- ✅ 3 templates principales: Inicio, Catálogo, Sección Administrativa

## 🔧 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/TU-USUARIO/techlogix.git
cd techlogix
```

### 2. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar PostgreSQL
Crear la base de datos en PostgreSQL:
```sql
CREATE DATABASE techlogix_db;
```

### 5. Configurar variables de entorno
Copiar `.env.example` a `.env` y ajustar credenciales:
```bash
cp .env.example .env
```

### 6. Ejecutar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Crear grupos, permisos y usuarios de prueba
```bash
python manage.py crear_grupos
```

### 8. Ejecutar el servidor
```bash
python manage.py runserver
```

Acceder a: `http://127.0.0.1:8000/`

## 👥 Usuarios de Prueba

| Rol | Usuario | Contraseña |
|-----|---------|------------|
| **Administrador** | `admin_tech` | `Admin1234!` |
| **Asistente** | `asistente_tech` | `Asist1234!` |

### Matriz de permisos:
| Acción | Anónimo | Asistente | Administrador |
|--------|---------|-----------|---------------|
| Ver Inicio | ✅ | ✅ | ✅ |
| Ver Catálogo | ✅ | ✅ | ✅ |
| Ver Panel Admin | ❌ | ✅ | ✅ |
| Crear/Editar/Eliminar | ❌ | ❌ | ✅ |

## 🤖 Uso de Inteligencia Artificial

Durante el desarrollo se utilizaron herramientas de IA (ChatGPT / Claude) para:

### Prompt 1 - Configuración PostgreSQL con variables de entorno
```
Necesito configurar Django 4.2 para conectar con PostgreSQL usando variables de entorno con python-decouple. 
Muéstrame el settings.py completo con las credenciales protegidas.
```
**Resultado:** Se utilizó para estructurar la sección `DATABASES` de forma segura.

### Prompt 2 - Mixins de permisos por grupo
```
Crea un mixin en Django que restrinja el acceso a una vista solo a usuarios que pertenezcan 
al grupo "Administrador", y otro mixin que permita acceso a "Administrador" y "Asistente".
```
**Resultado:** Se generaron `AdminRequiredMixin` y `AsistenteOrAdminRequiredMixin`.

### Prompt 3 - Depuración error de conexión PostgreSQL
```
Error: django.db.utils.OperationalError: FATAL: password authentication failed for user "postgres"
¿Cómo lo soluciono?
```
**Resultado:** Se verificó el archivo `.env` y las credenciales de PostgreSQL.

### Prompt 4 - Comando personalizado para crear grupos
```
Crea un comando de Django manage.py que cree dos grupos (Administrador y Asistente), 
asigne permisos CRUD sobre el modelo Producto al grupo Administrador y solo view al Asistente.
```
**Resultado:** Se creó el comando `crear_grupos.py`.

## 📂 Estructura del Proyecto
```
techlogix/
├── inventario/          # App con modelos, vistas, templates
├── techlogix/           # Configuración del proyecto
├── .env                 # Credenciales (NO subido)
├── requirements.txt
└── README.md
```

## 🧪 Pruebas Realizadas

- ✅ Conexión a PostgreSQL exitosa
- ✅ Migraciones aplicadas sin errores
- ✅ Login con usuarios de ambos roles
- ✅ CRUD completo como Administrador
- ✅ Asistente solo puede visualizar (botones C-U-D ocultos y bloqueados en backend)
- ✅ CSRF token presente en todos los formularios