from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": "Software Engineer",
    "location": "Mountain View",
    "salary": "Rs. 10,00,000",
  },
  {
    "id": 2,
    "title": "Data Scientist",
    "location": "Delhi, India",
    "salary": "Rs. 15,00,000",
  },
  {
    "id": 3,
    "title": "Front End Engineer",
    "location": "San Francisco, USA",
  },
  {
    "id": 4,
    "title": "Back End Engineer",
    "location": "Remote",
    "salary": "Rs. 14,00,000",
  }
]

@app.route("/")
def hello():
    return render_template("home.html", jobs=JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)