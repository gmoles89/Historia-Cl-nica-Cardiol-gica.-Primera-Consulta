 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a//dev/null b/app.py
index 0000000000000000000000000000000000000000..95bff16fec47409880d8929b8d064052f28bb920 100644
--- a//dev/null
+++ b/app.py
@@ -0,0 +1,15 @@
+from flask import Flask, render_template, request
+
+app = Flask(__name__)
+
+
+@app.route('/', methods=['GET', 'POST'])
+def index():
+    submitted_data = None
+    if request.method == 'POST':
+        submitted_data = request.form.to_dict(flat=False)
+    return render_template('index.html', submitted_data=submitted_data)
+
+
+if __name__ == '__main__':
+    app.run(debug=True)
 
EOF
)
