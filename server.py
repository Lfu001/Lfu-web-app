from flask import *
import math
import pandas as pd
import historyDB as db
import zuccumberNet as zn
from werkzeug.utils import secure_filename
import uuid
from datetime import datetime
import os

app = Flask(__name__)


@app.route("/")
def root():
    # myname = request.args.get("name")
    return render_template("home.html")


@app.route("/classification")
def image_classification():
    return render_template("classification.html")


@app.route("/classification/cucumber_zucchini", methods=["POST", "GET"])
def cucumber_zucchini():
    try:
        if request.method == "GET":
            return render_template("cucumber_zucchini.html")
        elif request.method == 'POST':
            f = request.files.get('file')
            filepath = secure_filename(f.filename)
            f.save(filepath)
            results = zn.predict(filepath)
            os.remove(filepath)
            return render_template("cucumber_zucchini.html", tables=[results.to_html(classes="data")], titles=results.columns.values)
        else:
            return abort(400)
    except Exception as e:
        return str(e)


@app.route("/area")
def link():
    return render_template("area.html")


@app.route("/area/circle")
def area_circle():
    radius = request.args.get("r", default=None, type=float)
    if radius is None:
        radius = 150
    answer = round(radius**2 * math.pi, 2)

    cookie = request.cookies.get("user_id", None)
    if cookie is None:
        user_id = str(uuid.uuid4())
    else:
        user_id = cookie

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db.addHistory("circle", [radius, answer, user_id, timestamp])
    table = pd.DataFrame(db.getHistory("circle", user_id), columns=["半径", "面積", "時刻"]).head(10).to_html(index=False)

    response = make_response(render_template("circle.html", radius=radius, answer=answer, table=table))
    max_age = 5
    expires = int(datetime.now().timestamp()) + max_age
    response.set_cookie('user_id', value=user_id, max_age=max_age, expires=expires, secure=None, httponly=False)

    return response


@app.route("/area/rectangle")
def area_rectangle():
    a = request.args.get("a", default=None, type=float)
    b = request.args.get("b", default=None, type=float)
    if a is None or b is None:
        a = 150
        b = 400
    answer = round(a * b, 2)

    cookie = request.cookies.get("user_id", None)
    if cookie is None:
        user_id = str(uuid.uuid4())
    else:
        user_id = cookie

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db.addHistory("rectangle", [a, b, answer, user_id, timestamp])
    table = pd.DataFrame(db.getHistory("rectangle", user_id), columns=["縦", "横", "面積", "時刻"]).head(10).to_html(index=False)

    response = make_response(render_template("rectangle.html", a=a, b=b, answer=answer, table=table))
    max_age = 5
    expires = int(datetime.now().timestamp()) + max_age
    response.set_cookie('user_id', value=user_id, max_age=max_age, expires=expires, secure=None, httponly=False)

    return response


# @app.route("/area/triangle")
# def area_triangle():
#    a = request.args.get("a", default=None, type=float)
#    answer = round(0.5 * a * a * (math.sqrt(3) * 0.5), 2)
#    return render_template("triangle.html", a=a, answer=answer)


@app.route("/hello")
def hello():
    return "hello"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 9761))
    app.run(debug=True, port=port, host="0.0.0.0")
