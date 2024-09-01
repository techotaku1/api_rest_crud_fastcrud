# CRUD con FastAPI y FastCRUD

## Descripción

Este proyecto muestra cómo construir una API CRUD completa utilizando **FastAPI** y **FastCRUD**. Incluye la configuración inicial y la implementación de endpoints para operaciones CRUD básicas.

Utilizar Base de datos **SQLITE**.

## Instalación

1. **Instala las dependencias:**

   ```bash
   pip install fastcrud
   ```
   ```bash
   pip install aiosqlite
   ```
   ```bash
   pip install sqlalchemy
   ```
   ```bash
   pip install fastapi
   ```
   ```bash
   pip install uvicorn
   ```

2. **Ejecuta la aplicación:**

   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

3. **Accede a la documentación:**

   Abre tu navegador y visita `http://localhost:8000/docs`.

## Uso

- **Crear:** `POST /personas`
- **Leer:** `GET /personas/{id}`
- **Actualizar:** `PUT /personas/{id}`
- **Eliminar:** `DELETE /personas/{id}`

## Créditos

Este proyecto utiliza [FastCRUD](https://github.com/igorbenav/fastcrud) para simplificar la creación de endpoints CRUD. Agradecemos al autor del repositorio de FastCRUD por proporcionar esta útil herramienta. @igorbenav

---

Este README proporciona instrucciones claras para instalar y ejecutar tu aplicación, junto con la información de uso y créditos apropiados.
