from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
	return '<h3>How to rapidly achieve awesomeness</h3>'
	
@app.route('/tree')
def tree():
	return '<h3>Got Wood</h3>'
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)