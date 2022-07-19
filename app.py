from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return """
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
    <li><a href='/animals/Dogs'>Dogs</a></li>
    <li><a href='/animals/Cats'>Cats</a></li>
    <li><a href='/animals/Rabbits'>Rabbits</a></li>
  </ul>
  """

@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f"""
  <h1>List of {pet_type}</h1>
  <a href='/'>Return to Home</a>
  """
  return html
