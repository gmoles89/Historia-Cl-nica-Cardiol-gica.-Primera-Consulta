from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    submitted_data = None
    if request.method == 'POST':
        submitted_data = request.form.to_dict(flat=False)
    return render_template('index.html', submitted_data=submitted_data)


if __name__ == '__main__':
    app.run(debug=True)
