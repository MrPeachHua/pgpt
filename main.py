from flask import Flask, render_template, request
import requests
from myopenai import gpt_content
import os
import openai
from gptmongo import insertOneGpt

app = Flask('app')
os.environ[
  "OPENAI_API_KEY"] = "sk-proj-Xy-XvQUXYk7OlQAgKHWVag3EPR8gKLdEroWR1WdxL-0QOM3z1VdqvJ9kr8T3BlbkFJk4mcYHsV4P_sVmF4tJrQt57SW48KBDnzVfDaDzBt4a9Bm9JbQd05R"
openai.api_key = "sk-proj-Xy-XvQUXYk7OlQAgKHWVag3EPR8gKLdEroWR1WdxL-0QOM3z1VdqvJ9kr8T3BlbkFJk4mcYHsV4P_sVmF4tJrQt57SW48KBDnzVfDaDzBt4a9Bm9JbQd05Rz"


@app.route('/')
def home():
  message = {"str": "hello"}
  return render_template('index.html', message=message)


@app.route('/idx')
def idx():
  message = {"str": "hello"}
  return render_template('index.html', message=message)


@app.route('/getContent', methods=['GET', 'POST'])
def getContent():
  input = ""
  print(request.remote_addr)
  try:
    input = request.form.get('input')
  except Exception as e:
    pass
  str = ""
  if input != "":
    str = gpt_content(input)
  # if str != "":
  #   try:
  #     insertOneGpt(input, str, request.remote_addr)
  #   except Exception as e:
  #     pass
  message = {"str": str}
  return render_template('index.html', message=message)


app.run(host='0.0.0.0', port=8080)
