# FastAPI + MongoDB + PostgreSQL Template
Plantilla inicial para proyectos web con FastAPI, MongoDB y PostgreSQL, pensada para acelerar el desarrollo y servir de referencia. 

> [!NOTE]  
> Esta plantilla refleja mis preferencias (JimcostDev). No garantiza que cubra todas las mejores prácticas, pero puede ser un excelente punto de partida.

> [!TIP]  
> Además, como es un template de GitHub, también puedes utilizarlo haciendo clic en el botón correspondiente para crear un nuevo repositorio basado en esta plantilla.

## 📋 Características
- Estructura de carpetas organizada
- Conexión asíncrona a **MongoDB** con `motor`
- Conexión asíncrona a **PostgreSQL** con `SQLAlchemy` + `asyncpg`
- Configuración mediante variables de entorno con `pydantic-settings`
- Hashing de contraseñas con `bcrypt` (o `aiobcrypt`)
- Autenticación basada en JWT con `python-jose`
- Suite de tests con `pytest` y `pytest-asyncio`

## 🚀 Instrucciones de Uso

1. **Clona este repositorio** ejecutando el siguiente comando:

    ```bash
    git clone https://github.com/JimcostDev/fastapi-mongo-template.git
    ```

2. **Crea y activa tu entorno virtual**:

    - Crea un entorno virtual:

        ```bash
        python -m venv venv
        ```

    - Activa el entorno virtual:

        - En **Windows**:

            ```bash
            venv\Scripts\activate
            ```

        - En **macOS y Linux**:

            ```bash
            source venv/bin/activate
            ```

3. **Instala las dependencias requeridas**:
    - Instalar todas con `requirements.txt`:
        ```bash
        pip install -r requirements.txt
        ```
    - Instalar dependencias individuales (opcional):
        ```bash
        pip install "fastapi[standard]" motor pymongo asyncpg sqlalchemy pytest pytest-asyncio pydantic-settings aiobcrypt python-jose
        ```

---

## 🛠️ Configuración de Base de Datos

> [!IMPORTANT]  
> Debes configurar correctamente las variables de entorno en tu archivo `core/config.env` o exportarlas en tu sistema.

### ⚙️ Configuración MongoDB

```sh
MONGODB_URI_DEV_LAB_TEST=mongodb+srv://user:password@server/
MONGODB_NAME=db_name
```

### ⚙️ Configuración PostgreSQL

```sh
POSTGRES_URI=postgresql+asyncpg://user:password@localhost:5432/db_name
```

### ⚙️ Configuración JWT

```sh
JWT_SECRET_KEY=secreto-muy-secreto
```

---

4. **Ejecuta el servidor**:

    Inicia el servidor en modo de desarrollo o producción:

    - Modo **desarrollo**:
        ```bash
        fastapi dev main.py
        ```

    - Modo **producción**:
        ```bash
        fastapi run
        ```

5. **Actualizar versión de FastAPI** (opcional):
    ```bash
    pip install --upgrade fastapi
    ```

6. **Documentación oficial**: [FastAPI](https://fastapi.tiangolo.com/#requirements)

---

> [!TIP]  
> ¡Si te resulta útil este proyecto, apóyalo con una ⭐! Tu apoyo nos motiva a crear más contenido y mejorar los recursos disponibles. ¡Gracias! :octocat:
