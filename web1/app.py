from flask import Flask, render_template
app = Flask(__name__)

poems = [
    {
        "title": "Thơ con cóc",
        "content": "Hôm nay trăng lên cao quá",
        "author": "Huế",
        "gender": "female",
    },
    {
        "title": "Thơ con ếch",
        "content": "Để thằng bán đồ giữ mất tuổi thanh xuân",
        "author": "Trường",
        "gender": "male",
    },
]

@app.route('/')
def index():
    return "Hello C4E27"

@app.route('/say-hi/<name>')
def sayhi(name):
    return "Hi " + name

@app.route('/sum/<int:num1>/<int:num2>')
def sum(num1,num2):
    return str(num1 + num2) 

@app.route('/poem')
def poem():
    return render_template("poem.html", poems = poems)

@app.route('/poem/<int:index>')
def detail(index):
    poem = poems[index]
    return render_template("poem-detail.html", poem = poem, index = index)

if __name__ == '__main__':
  app.run(debug=True)
 