from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

from flask import Flask, render_template, request


app = Flask(__name__)


@dataclass
class Section:
    title: str
    fields: List[Tuple[str, str]]
    multiline: bool = False


FIELD_TYPES: Dict[str, str] = {
    "edad": "number",
    "fecha_consulta": "date",
    "peso": "number",
    "talla": "number",
    "imc": "number",
    "presion_arterial": "text",
    "frecuencia_cardiaca": "number",
    "saturacion": "number",
}


SECTIONS: List[Section] = [
    Section(
        "Datos del paciente",
        [
            ("nombre", "Nombre"),
            ("documento", "Documento"),
            ("edad", "Edad"),
            ("sexo", "Sexo"),
            ("fecha_consulta", "Fecha de la consulta"),
            ("contacto", "Datos de contacto"),
            ("obra_social", "Cobertura/Obra social"),
        ],
    ),
    Section(
        "Antecedentes personales y factores de riesgo",
        [
            ("antecedentes", "Antecedentes personales relevantes"),
            ("factores_riesgo", "Factores de riesgo"),
            ("antecedentes_familiares", "Antecedentes familiares"),
            ("factores_riesgo_extra", "Otros factores/Comentarios"),
        ],
        multiline=True,
    ),
    Section(
        "Motivo de consulta y enfermedad actual",
        [
            ("motivo_consulta", "Motivo de consulta"),
            ("enfermedad_actual", "Enfermedad actual"),
        ],
        multiline=True,
    ),
    Section(
        "Tratamientos habituales, alergias y hábitos",
        [
            ("medicacion", "Medicación habitual"),
            ("alergias", "Alergias"),
            ("habitos", "Hábitos (tabaquismo, alcohol, actividad física, dieta)"),
        ],
        multiline=True,
    ),
    Section(
        "Datos biométricos",
        [
            ("peso", "Peso (kg)"),
            ("talla", "Talla (cm)"),
            ("imc", "IMC"),
            ("presion_arterial", "Presión arterial"),
            ("frecuencia_cardiaca", "Frecuencia cardíaca"),
            ("saturacion", "Saturación O2"),
        ],
    ),
    Section(
        "Examen físico",
        [("examen_fisico", "Hallazgos del examen físico")],
        multiline=True,
    ),
    Section(
        "Estudios complementarios",
        [
            ("estudios_previos", "Estudios previos"),
            ("estudios_actuales", "Estudios actuales/relevantes"),
        ],
        multiline=True,
    ),
    Section(
        "Conclusión diagnóstica y plan",
        [
            ("impresion_diagnostica", "Impresión diagnóstica"),
            ("conducta", "Conducta terapéutica"),
            ("analiticas", "Laboratorios o estudios solicitados"),
            ("seguimiento", "Plan de seguimiento"),
        ],
        multiline=True,
    ),
]


def build_summary(form_data: Dict[str, str]) -> str:
    """Genera un resumen de la historia clínica a partir de los datos del formulario."""

    lines: List[str] = ["Historia Clínica Cardiológica - Primera Consulta", ""]

    for section in SECTIONS:
        section_lines: List[str] = []
        for key, label in section.fields:
            value = form_data.get(key, "").strip()
            if not value:
                continue
            if section.multiline:
                section_lines.append(f"{label}:\n{value}")
            else:
                section_lines.append(f"{label}: {value}")

        if section_lines:
            lines.append(section.title + ":")
            for section_line in section_lines:
                if "\n" in section_line:
                    label, text = section_line.split(":\n", 1)
                    lines.append(f"- {label}:")
                    for paragraph in text.splitlines():
                        if paragraph.strip():
                            lines.append(f"    {paragraph.strip()}")
                        else:
                            lines.append("")
                else:
                    lines.append(f"- {section_line}")
            lines.append("")

    return "\n".join(lines).strip()


def clean_form_data(raw_data: Dict[str, str]) -> Dict[str, str]:
    cleaned: Dict[str, str] = {}
    for key, value in raw_data.items():
        cleaned[key] = value.strip()
    factores_seleccionados = request.form.getlist("factores_riesgo_check")
    extra = raw_data.get("factores_riesgo", "").strip()
    if factores_seleccionados or extra:
        resumen_factores = [factor for factor in factores_seleccionados if factor]
        if extra:
            resumen_factores.append(extra)
        cleaned["factores_riesgo"] = "; ".join(resumen_factores)
    cleaned.pop("factores_riesgo_check", None)
    return cleaned


@app.route("/", methods=["GET", "POST"])
def index():
    summary: str | None = None
    cleaned_data: Dict[str, str] = {}

    if request.method == "POST":
        raw_data = request.form.to_dict()
        cleaned_data = clean_form_data(raw_data)
        summary = build_summary(cleaned_data)

    return render_template(
        "index.html",
        summary=summary,
        form_data=cleaned_data,
        sections=SECTIONS,
        field_types=FIELD_TYPES,
    )


if __name__ == "__main__":
    app.run(debug=True)
