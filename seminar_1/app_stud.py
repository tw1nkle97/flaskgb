from flask import Flask, render_template

app = Flask(__name__)

stud = [
    {"name": 'John', "surname": 'Smith', "age": 25, "avg_score": 3.4},
    {"name": 'John', "surname": 'Konstantin', "age": 120, "avg_score": 4.9},
    {"name": 'Eva', "surname": 'Pola', "age": 31, "avg_score": 4.1}
]

news = [
    {"title": 'Подледная рыбалка', "date": '2023-02-12', "text": 'Lorem ipsum dolor, sit amet consectetur adipisicing '
                                                                 'elit. Porro deleniti quidem nostrum unde consectetur'
                                                                 ' ut animi tenetur consequatur natus aspernatur.'},
    {"title": 'Java', "date": '2023-05-18', "text": 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. '
                                                    'Porro deleniti quidem nostrum '},
    {"title": 'Python', "date": '2022-12-31', "text": 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. '
                                                      'Porro deleniti quidem nostrum unde consectetur ut '},
    {"title": 'SCSS', "date": '2020-04-20', "text": 'Porro deleniti quidem nostrum unde consectetur ut animi tenetur '
                                                    'consequatur natus aspernatur.'}
]

@app.route('/')
def students():
    return render_template('students.html', stud=stud)


@app.route('/news/')
def news_page():
    return render_template('news.html', news=news)

if __name__ == '__main__':
    app.run()
