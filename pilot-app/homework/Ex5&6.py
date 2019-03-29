from flask import Flask, render_template
from mlab import rivers_collection
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/river')
def all_river():
    rivers = rivers_collection.find()
    continent_list = []
    for river in rivers:
      if river["continent"] not in continent_list:
        continent_list.append(river["continent"])
    return render_template('all-rivers.html',rivers = rivers,continent_list = continent_list)

@app.route('/river/<continent>')
def river(continent):
    continent_rivers = rivers_collection.find({"continent": continent})
    return render_template('continent_rivers.html',continent_rivers = continent_rivers)

if __name__ == '__main__':
  app.run(debug=True)
 