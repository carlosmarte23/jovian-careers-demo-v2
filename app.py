from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)

@app.route("/")
def hello():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs)

@app.route("/api/jobs")
def get_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if job is None:
    return "Not found", 404
  else:
    return render_template("jobpage.html", job=job)

@app.route("/job/<id>/apply", methods=["POST"])
def apply_job(id):
  job = load_job_from_db(id)
  # Store in db
  data = request.form
  print("Form data:", data)
  add_application_to_db(id, data)
  # Send email
  # Acknowledgement submition
  return render_template("application_submitted.html", application=data, job=job)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)