# FastAPI MongoDB Template
Esta plantilla está diseñada para trabajar con **FastAPI** y **MongoDB**. Proporciona una estructura de carpetas organizada y funcional para acelerar el desarrollo de nuevos proyectos. 

Es importante aclarar que esta plantilla ha sido creada bajo mis gustos y preferencias personales (JimcostDev). No asegura que siga las mejores prácticas ni que sea el enfoque correcto para todos los proyectos. Sin embargo, puede ser útil como punto de partida o referencia.

> !Si te resulta útil este proyecto, apóyalo con una ⭐! Tu apoyo nos motiva a crear más contenido y mejorar los recursos disponibles. ¡Gracias! :octocat:

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

    Asegúrate de configurar correctamente la conexión a MongoDB en el archivo `database/conn_db.py`. Puedes utilizar variables de entorno para las credenciales y la URL de MongoDB.

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
    pip install "fastapi[standard]"
    pip install pymongo
    ```
8. **Documentación** [FastAPI:](https://fastapi.tiangolo.com/#requirements)
## Uso del Template en GitHub
Además, como es un template de GitHub, también puedes utilizarlo haciendo clic en el botón correspondiente para crear un nuevo repositorio basado en esta plantilla.
