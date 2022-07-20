from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  return """
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
    <li><a href='/animals/dogs'>dogs</a></li>
    <li><a href='/animals/cats'>cats</a></li>
    <li><a href='/animals/rabbits'>rabbits</a></li>
  </ul>
  """

@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f"""
  <h1>List of {pet_type}</h1>
  <a href='/'>Return to Home</a>
  """ 
  html += "<ul>"
  for i in pets[pet_type]:
    html += f"<li>{i['name']}</li>"
  html += "<ul>"
  return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]

  return f"<h1>{pet['name']}"
