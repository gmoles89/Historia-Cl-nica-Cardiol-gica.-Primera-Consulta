# Historia Clínica Cardiológica - Primera Consulta

Aplicación web simple desarrollada con Flask que permite registrar datos de una historia clínica cardiológica de un paciente.

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
