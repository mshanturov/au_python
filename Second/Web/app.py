import math
from flask import Flask, render_template, request, url_for

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/test')
def test():
    if request.method == 'GET':
        n=request.args.get('name')
    if n==None:
        n=""
    else:
        n=int(n)
        if (math.factorial(n-1)+1) % n!=0:
            return render_template(
                'test.html',
        name="составное")
        else:
            return render_template(
                'test.html',
        name="простое")
    return render_template(
        'test.html',
        name=n)


if __name__ == "__main__":
    app.run()