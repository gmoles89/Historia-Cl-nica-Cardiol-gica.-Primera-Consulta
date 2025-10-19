# Historia Clínica Cardiológica - Primera Consulta

Aplicación web simple desarrollada con Flask que permite registrar datos de una historia clínica cardiológica de un paciente.

## Descargar los archivos

Puedes obtener todo el proyecto dentro de una carpeta de dos maneras:

1. **Clonar el repositorio con Git** (mantiene el historial y facilita futuras actualizaciones):

   ```bash
   git clone https://github.com/<TU_USUARIO>/Historia-Cl-nica-Cardiol-gica.-Primera-Consulta.git
   ```

   El comando creará una carpeta llamada `Historia-Cl-nica-Cardiol-gica.-Primera-Consulta` con todos los archivos.

2. **Descargar un archivo ZIP** (no requiere tener Git instalado):

   - Haz clic en el botón **Code** en la página del repositorio.
   - Selecciona la opción **Download ZIP**.
   - Descomprime el archivo descargado; se generará una carpeta que contendrá todos los archivos del proyecto.

Una vez descargados, puedes mover la carpeta resultante a donde prefieras dentro de tu equipo y continuar con los pasos de instalación.

## Requisitos

- Python 3.9 o superior
- pip

## Instalación

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución

```bash
flask --app app run
```

La aplicación estará disponible en `http://127.0.0.1:5000/`.

## Estructura del formulario

El formulario está dividido en secciones para datos del paciente, medicación habitual, examen físico, exámenes complementarios y evaluación/indicaciones.
