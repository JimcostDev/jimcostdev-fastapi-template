# FastAPI + MongoDB Template
Plantilla inicial para proyectos web con FastAPI y MongoDB, pensada para acelerar el desarrollo y servir de referencia. 

> [!NOTE]
> Esta plantilla refleja MIS preferencias (JimcostDev). No garantiza que cubra todas las mejores prácticas, pero puede ser un excelente punto de partida.

> [!INFO]
> Además, como es un template de GitHub, también puedes utilizarlo haciendo clic en el botón correspondiente para crear un nuevo repositorio basado en esta plantilla.

> [!TIP] 
> !Si te resulta útil este proyecto, apóyalo con una ⭐! Tu apoyo nos motiva a crear más contenido y mejorar los recursos disponibles. ¡Gracias! :octocat:

## 📋 Características
- Estructura de carpetas organizada
- Conexión asíncrona a MongoDB con motor
- Configuración mediante variables de entorno con pydantic-settings
- Hashing de contraseñas con bcrypt (o aiobcrypt)
- Autenticación basada en JWT con python-jose
- Suite de tests con pytest y pytest-asyncio

## Instrucciones de Uso

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

    ```bash
    pip install -r requirements.txt
    ```

4. **Configura la conexión a MongoDB**:

    Asegúrate de configurar correctamente la conexión a MongoDB en el archivo `core/cofig.env`. Puedes utilizar variables de entorno para las credenciales y la URL de MongoDB. Por ejemplo:
     ```bash
    MONGODB_URI_DEV_LAB_TEST=mongodb+srv://user:password@server/
    MONGODB_NAME=db_name
    JWT_SECRET_KEY=secreto-muy-secreto
    ```

5. **Ejecuta el servidor**:

    Inicia el servidor en modo de desarrollo o producción:

    - Modo **desarrollo**:

        ```bash
        fastapi dev main.py
        ```

    - Modo **producción**:

        ```bash
        fastapi run
        ```

6. **Actualizar versión de FastAPI** (opcional):

    ```bash
    pip install --upgrade fastapi
    ```

7. **Instalar dependencias individuales** (opcional):

    ```bash
    pip install "fastapi[standard]" motor pymongo pytest pytest-asyncio pydantic-settings aiobcrypt python-jose
    ```
8. **Documentación** [FastAPI:](https://fastapi.tiangolo.com/#requirements)
   

