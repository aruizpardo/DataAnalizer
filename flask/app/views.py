from app import app
from datetime import datetime
from flask import jsonify, render_template, request
from sqlalchemy import create_engine

import pandas as pd

import sys


def insert_data(table, values):
   insert = create_engine('clickhouse://default:bPt0Y/GIB7oxsJX9@clickhouse/default')
   print(values, file=sys.stderr)
   data = pd.DataFrame(data=values)
   try:
      data.to_sql(name=table, con=insert, if_exists='append', index=False)
      return True
   except Exception:
      return False


@app.route('/')
def home():
   return render_template('home.html')


@app.route('/data_gastos')
def data_gastos():
   return render_template('data_gastos.html')


@app.route('/data_bascula')
def data_bascula():
   return render_template('data_bascula.html')


@app.route('/insert_data_gastos', methods=["POST"])
def insert_data_gastos():
   values = {
      'motivo': [request.form.get('motivo')],
      'cantidad': [float(request.form.get('cantidad'))],
      'categoria': [request.form.get('categoria')],
      'fecha': [datetime.strptime(request.form.get('fecha'), '%Y-%m-%d').date()],
      'necesario': [1 if request.form.get('necesario') else 0]
   }

   return render_template('success_insert_data.html') if insert_data('gastos', values) else render_template('fail_insert_data.html')


@app.route('/insert_data_bascula', methods=["POST"])
def insert_data_bascula():
   values = {
      'grasa_corporal': [request.form.get('grasa_corporal')],
      'agua': [request.form.get('agua')],
      'proteina': [request.form.get('proteina')],
      'metabolismo_basal': [request.form.get('metabolismo_basal')],
      'grasa_visceral': [request.form.get('grasa_visceral')],
      'musculo': [request.form.get('musculo')],
      'masa_osea': [float(request.form.get('masa_osea'))],
      'peso': [request.form.get('peso')],
      'fecha': [datetime.strptime(request.form.get('fecha'), '%Y-%m-%d').date()]
      }

   return render_template('success_insert_data.html') if insert_data('bascula', values) else render_template('fail_insert_data.html')


@app.route('/healthcheck')
def healthcheck():
   response = jsonify(health="ok")
   response.status_code = 200
   return response