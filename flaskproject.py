from flask import Flask, render_template




app = Flask(__name__)

posts = [
    {
        'author': 'rami',
        'title': 'ramis post',
        'content': 'first post by rami'
        },
        {
        'author': 'mary',
        'title': 'marys post',
        'content': 'first post by mary'
        }
    ]




@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',posts=posts)




if __name__ == '__main__':
    app.run(debug=True)


    
