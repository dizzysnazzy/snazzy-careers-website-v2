from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)



@app.route("/")
def hello_snazzy():
  jobs=load_jobs_from_db()
  #return "Hello, world"
  #return render_template('home.html')
  return render_template('home.html',
                         jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  jobs=load_jobs_from_db()
  return jsonify(jobs)

@app.route("/jobs/<id>")
def show_job(id):
  job=load_job_from_db(id)
  
  if not job:
    return "Not Found", 404
    
  return render_template('jobpage.html',
                         job=job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):  
  data = request.form
  job=load_job_from_db(id)
  add_application_to_db(id, data)
  # store this in the db
  # send an email
  # display an acknowledgement
  return render_template('application_submitted.html',
                         application=data,
                         job=job)

@app.route("/about")
def about_snazzy():
  # jobs=load_jobs_from_db()
  return render_template('about.html')
  # return render_template('home.html',
  #                        jobs=jobs)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)