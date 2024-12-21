from flask import Flask, render_template, request

app = Flask(__name__)

def c_grade(rank, total):
    percentage = (rank / total) * 100

    if percentage <= 4.0:
        return 1
    elif percentage <= 11.0:
        return 2
    elif percentage <= 23.0:
        return 3
    elif percentage <= 40.0:
        return 4
    elif percentage <= 60.0:
        return 5
    elif percentage <= 77.0:
        return 6
    elif percentage <= 89.0:
        return 7
    elif percentage <= 96.0:
        return 8
    else:
        return 9

@app.route("/", methods=["GET", "POST"])
def index():
    grade = None
    subject = None
    total = None
    rank = None

    if request.method == "POST":
        subject = request.form["subject"]
        total = int(request.form["total"])
        rank = int(request.form["rank"])
        grade = c_grade(rank, total)

    return render_template("index.html", grade=grade, subject=subject, total=total, rank=rank)

if __name__ == "__main__":
    app.run(debug=True)
