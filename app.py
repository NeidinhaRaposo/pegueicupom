#====================================================== BIBLIOTECAS ==================================================

from flask import Flask, render_template, jsonify, json
import _sqlite3 as db
import os


app = Flask(__name__, static_folder='static', template_folder='templates')

# UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')

# ==================================================== Front-End =====================================================
@app.route('/')
def index():
    return render_template('index.html')






if __name__ == '__main__':
    app.run(debug=True, port=8000)
