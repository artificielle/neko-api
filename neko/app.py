from flask import Flask

# pylint: disable=invalid-name
app = Flask(__name__)

@app.route('/')
def index():
  return 'It works'

if __name__ == '__main__':
  app.run(debug=True)
