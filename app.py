from flask import Flask, render_template
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
    return render_template('home.html',jobs = JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)