import requests
from secrettt import secretsny
from flask import Flask, render_template

cc = secretsny()
NYTimes_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
params = {'api-key': cc.api_key}
nytime_response = requests.get(NYTimes_url, params)
nytime_response_js = nytime_response.json()
top_tpic_list = []
for i in range(0, 5):
    top_tpic_list.append(nytime_response_js['results'][i]['title'])



app = Flask(__name__)
@app.route('/')
def welcome():
    return "<h1>Welcome!</h1>"

@app.route('/name/<nm>')
def name(nm):
    return render_template('name.html', name=nm)

@app.route("/headline/<nm>")
def headline(nm):
    return render_template('headlines.html', name=nm, headlines=top_tpic_list)



if __name__ == '__main__':
    app.run(debug=True)
