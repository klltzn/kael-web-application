from flask import Flask, render_template,url_for, jsonify

app = Flask(__name__)


JOBS = [
  {
    'id' : 1,
    'title' : 'Data Analyst',
    'location' : 'Cebu, Philippines',
    'salary' : '50,000 pesos per month'
  },
  {
    'id' : 2,
    'title' : 'Software Engineer',
    'location' : 'Australia',
    'salary' : '$100,000 anually'
  },
  {
    'id' : 3,
    'title' : 'Cybersecurity Engineer',
    'location' : 'United States of America',
    'salary' : '$300,000 per year'
  },
  {
    'id' : 4,
    'title' : 'Backend Engineer',
    'location' : 'Tokyo, Japan',
    'salary' : '$20,000 per month'
  },
]



@app.route("/")
def hello_world():
  return render_template('home.html',
                         jobs=JOBS,
                         company_name='Python')

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)