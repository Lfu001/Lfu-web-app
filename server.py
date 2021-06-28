from flask import *
import math

app = Flask(__name__)

@app.route("/")
def root():
    myname = request.args.get("name")
    return render_template("home.html")

@app.route("/area")
def link():
    return render_template("area.html")

@app.route("/area/circle")
def area_circle():
    radius = request.args.get("r", default=None, type=float)
    answer = round(radius**2 * math.pi, 2)
    return render_template("circle.html", radius=radius, answer=answer)

@app.route("/area/rectangle")
def area_rectangle():
    a = request.args.get("a", default=None, type=float)
    b = request.args.get("b", default=None, type=float)
    answer = round(a * b, 2)
    return render_template("rectangle.html", a=a, b=b, answer=answer)

#@app.route("/area/triangle")
#def area_triangle():
#    a = request.args.get("a", default=None, type=float)
#    answer = round(0.5 * a * a * (math.sqrt(3) * 0.5), 2)
#    return render_template("triangle.html", a=a, answer=answer)

@app.route("/hello")
def hello():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True, port=9761)