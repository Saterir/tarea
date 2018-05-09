from flask import Flask, redirect, url_for, request, render_template, jsonify
import sys
import os
import uuid
import urllib.request

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])

def inicio():
    data = None
    if request.method == 'POST':
        data = request.json
        try:
            return render_template('respuesta.html', respuesta = data['respuesta'])
        except Exception as e:
            return e
    else:
        return render_template('inicio.html')
if __name__ == '__main__':
   app.run(host='0.0.0.0',debug = True , port = 5000)