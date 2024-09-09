from flask import Flask, jsonify, render_template,request
from sqlalchemy import text
from database import load_jobs,load_job_from_db,add_application_to_db
app = Flask(__name__)

JOBS = [{'id':1,
        'title':'Data Scientist',
        'location':'Delhi',
        'salary':'Rs 20,00,000'},
       {'id':2,
           'title':'Data Analyst',
           'location':'Bangalore',
           'salary':'Rs 25,00,000'},
       {'id':3,
              'title':'Manager',
              'location':'Kashmir',
       },
       {'id':4,
             'title':'Admin',
             'location':'North Pole',
             'salary':'Rs 75,00,000'}]



    

    
@app.route('/')
def hello_world():
    jobs = load_jobs()
    return render_template('home.html',jobs = jobs)

@app.route('/jobs/<id>')
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found",404
    return render_template('jobspage.html',job = job)

@app.route('/jobs/<id>/apply',methods=['post'])
def apply_to_jobs(id):
    data = request.form
    add_application_to_db(id,data)
    return render_template('application_submited.html',application=data)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)