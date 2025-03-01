# Proyecto Final de POO - Backend

Este es el repositorio del proyecto final de Programación Orientada a Objetos (POO). El objetivo de este proyecto es desarrollar el backend de una aplicación utilizando diversas tecnologías y buenas prácticas de desarrollo.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal para el desarrollo del backend.
- **FastAPI**: Framework para la creación de aplicaciones web rápidas y eficientes.
- **PostgreSQL**: Sistema de gestión de bases de datos relacional. (En implementación)
- **Pytest**: Framework para la realización de pruebas unitarias. (Por agregar)
- **SQLAlchemy**: ORM para la interacción con la base de datos.
- **Cython**: Herramienta para la compilación de código C en módulos de extensión de Python.
- **Passlib**: Biblioteca para el manejo de contraseñas, incluyendo soporte para bcrypt.
- **PyJWT**: Biblioteca para la codificación y decodificación de JSON Web Tokens.

## Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instalados los siguientes componentes:

- Python 3.8 o superior
- PostgreSQL 13 o superior
- Git (para clonar el repositorio)

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/DazJ14/poo_proyectofinal_backend.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd poo_proyectofinal_backend
    ```
3. **Nota**: Antes de continuar, asegúrate de crear y activar un entorno virtual. Consulta la sección [Creación de un Entorno Virtual](#creación-de-un-entorno-virtual) más abajo.
4. Configura la base de datos en un archivo `.env`. Crea un archivo llamado `.env` en el directorio raíz del proyecto y agrega la siguiente línea, reemplazando `<TU_DATABASE_URL>` con la cadena de conexión a tu base de datos PostgreSQL:
    ```plaintext
    DATABASE_URL=<TU_DATABASE_URL>
    ```
5. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
6. Ejecuta el proyecto:
    ```bash
    python src/main.py
    ```

## Creación de un Entorno Virtual

Para aislar las dependencias del proyecto y evitar conflictos con otras instalaciones de Python, se recomienda crear un entorno virtual. Si ya tienes un entorno virtual configurado, puedes saltarte esta sección.

1. Navega al directorio del proyecto:
    ```bash
    cd poo_proyectofinal_backend
    ```
2. Crea un entorno virtual:
    ```bash
    python -m venv venv
    ```
3. Activa el entorno virtual:

    - En Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - En macOS y Linux:
        ```bash
        source venv/bin/activate
        ```

4. Verifica que el entorno virtual está activado. Deberías ver el nombre del entorno (por ejemplo, `(venv)`) al inicio de la línea de comandos. En caso de querer seguir con la instalación, consulta la sección [Pasos de instalación](#instalación).

5. Para desactivar el entorno virtual, utiliza el siguiente comando una vez que hayas finalizado tus tareas:
    ```bash
    deactivate
    ```

## To Do

- [ ] Crear middlewares para autenticacion.
- [ ] Revisar cómo hacer que una persona sin bash pueda instalar las dependencias
- [ ] Agregar pruebas unitarias con Pytest
- [ ] Implementar encriptación de contraseñas en la base de datos
- [ ] Configurar autenticación con JWT
- [ ] Modificar el proyecto para que sea orientado a objetos