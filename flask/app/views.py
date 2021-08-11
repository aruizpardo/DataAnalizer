from app import app
from flask import jsonify, render_template, request
import pandas as pd

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/insert_data', methods=["POST"])
def insert_data():
   motivo = request.form.get('motivo')
   cantidad = request.form.get('cantidad')
   categoria = request.form.get('categoria')
   necesario = True if request.form.get('necesario') else False

   return render_template('success_insert_data.html', motivo=motivo, cantidad=cantidad, categoria=categoria, necesario=necesario)

@app.route('/healthcheck')
def healthcheck():
   response = jsonify(health="ok")
   response.status_code = 200
   return response