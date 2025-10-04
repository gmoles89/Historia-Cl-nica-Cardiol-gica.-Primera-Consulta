 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/README.md b/README.md
index 3dbacd5c3a8fb9f32ff8d0efc77a491f2070c23f..439490dcf58f38bd8c8bca8d44e2c49c8d006f8c 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,28 @@
-# Historia-Cl-nica-Cardiol-gica.-Primera-Consulta
+# Historia Clínica Cardiológica - Primera Consulta
+
+Aplicación web simple desarrollada con Flask que permite registrar datos de una historia clínica cardiológica de un paciente.
+
+## Requisitos
+
+- Python 3.9 o superior
+- pip
+
+## Instalación
+
+```bash
+python -m venv venv
+source venv/bin/activate  # En Windows: venv\Scripts\activate
+pip install -r requirements.txt
+```
+
+## Ejecución
+
+```bash
+flask --app app run
+```
+
+La aplicación estará disponible en `http://127.0.0.1:5000/`.
+
+## Estructura del formulario
+
+El formulario está dividido en secciones para datos del paciente, medicación habitual, examen físico, exámenes complementarios y evaluación/indicaciones.
 
EOF
)
