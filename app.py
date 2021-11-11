import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename
from PIL import Image, ImageFilter, ImageEnhance
from utils import tokenizer, model

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def my_form(chat = ''):
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    print('user:', text)
    inputs = tokenizer(text, return_tensors="pt")
    res = model.generate(**inputs)
    reply = tokenizer.decode(res[0])
    reply = reply.replace('<s>', '')
    reply = reply.replace('</s>', '')
    print('bot:', reply)
    return my_form(text)

app.run()