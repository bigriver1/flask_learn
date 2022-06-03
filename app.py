from flask import Flask, jsonify, url_for, redirect, request,render_template
import config

app = Flask(__name__)

app.config.from_object(config)

# @app.route('/')
# def hello_world():
#     return {"username" : "俊杰123"}

book_list = [
    {"id": 1, "name": "三国演义"},
    {"id": 2, "name": "水浒传"},
    {"id": 3, "name": "红楼梦"},
    {"id": 4, "name": "西游记"},

]


@app.route('/book/detail/<int:book_id>')
def book_detail(book_id):
    print(book_id)
    for book in book_list:
        if book_id == book['id']:
            return book['name']

    return f'book_id为{book_id} 的图书不存在!'


@app.route('/book/list')
def book():
    for book in book_list:
        book['url'] = url_for("book_detail", book_id=book["id"])
    return jsonify(book_list)


@app.route('/profile')
def profile():
    user_id = request.args.get('id')
    if user_id:
        return '个人用户中心'
    return redirect(url_for('index'))

@app.route('/course')
def course():
    course_other = {
        "course_name": "flask"
    }
    return render_template('course.html', **course_other)

@app.route('/')
def index():
    return 'Hello Wordl!'


if __name__ == '__main__':
    app.run()
