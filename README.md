# Historia Clínica Cardiológica - Primera Consulta

Aplicación web construida con Flask para documentar de forma ágil la historia clínica cardiológica en la primera consulta. El formulario integra secciones estructuradas y calculadoras clínicas habituales (CHA<sup>2</sup>DS<sub>2</sub>-VASc, RCRI, CKD-EPI 2021 y Framingham) y genera un resumen listo para copiar o compartir.

## Requisitos

- Python 3.10 o superior
- pip

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución

```bash
flask --app app run --debug
```

La aplicación quedará disponible en `http://127.0.0.1:5000/`.

## Funcionalidades

- Formulario dividido en secciones: datos del paciente, antecedentes, motivo de consulta, enfermedad actual, medicación, alergias, datos biométricos, examen físico, estudios, conclusión diagnóstica y plan terapéutico.
- Calculadoras de soporte clínico basadas en modelos reconocidos:
  - CHA<sup>2</sup>DS<sub>2</sub>-VASc.
  - CKD-EPI 2021 para estimar la tasa de filtrado glomerular.
  - Índice de Riesgo Cardíaco Revisado (RCRI) prequirúrgico.
  - Riesgo cardiovascular a 10 años (modelo de Framingham 2008).
- Generación automática de un resumen en texto plano listo para copiar o pegar en la historia clínica electrónica.
- Cálculo automático del IMC a partir de peso y talla.

## Estructura del proyecto

```
├── app.py              # Aplicación Flask y generación del resumen
├── requirements.txt    # Dependencias del proyecto
├── static/
│   └── styles.css      # Estilos principales de la interfaz
└── templates/
    └── index.html      # Plantilla principal con formulario y calculadoras
```

## Licencia

Este proyecto se distribuye bajo la Licencia MIT.
