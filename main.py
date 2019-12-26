from flask import Flask,render_template

app = Flask(__name__)

@app.route("/shopping")
def shopping():
    food = ["cheese", "burger", "pizza"]
    return render_template("shopping.html" , food=food)


if __name__ == "__main__":
    app.run(debug=True)