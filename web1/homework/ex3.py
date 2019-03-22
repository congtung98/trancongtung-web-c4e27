from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<user_name>')
def user(user_name):
    Users = {
        "tung": {
            "name": "Trần Công Tùng",
            "age": 21,
            "gender": "Male",
            "hobby": "Auto Chess",
        },
        "nhat": {
            "name": "Nguyễn Quang Nhật",
            "age": 20,
            "gender": "Male",
            "hobby": "Fap",
        },
        "huyanh": {
            "name": "Nguyễn Huy Anh",
            "age": 21,
            "gender": "Female",
            "hobby": "Dota2",
        },
        "hai": {
            "name": "Phạm Thanh Hải",
            "age": 21,
            "gender": "Gay",
            "hobby": "Gym",
        },
    }
    if user_name in Users:
        user_name = Users[user_name]
        return render_template('user.html',user_name = user_name)
    else:
        return "User not found"

if __name__ == '__main__':
  app.run(debug=True)
 