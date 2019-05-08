from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

#dummy data
contacts = [
	{
		'id': 1,
		'name': 'Alanna',
		'address': '666 Sesame Street',
		'city': 'Portland',
		'state': 'OR',
		'zip': 97217
	},
	{
		'id': 2,
		'name': 'Tom Risse',
		'address': '664 Sesame Street',
		'city': 'San Francisco',
		'state': 'CA',
		'zip': 97212
	}
]


@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		data = request.form
		return render_template('index.html', data = data)
	#if no POST method, return user home, should be error message in real life
	return render_template('index.html')

# gets all the avilabale contacts, right now just dummy data
@app.route('/contacts', methods=['GET'])
def contacts():
	data = contacts
	return render_template('contacts.html', data = data)

#renders the form template for creating a new contact
@app.route('/new_contact')
def new_contact():
	return render_template('new_contact.html')

#returns the form data from creating a new contact
@app.route('/result', methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		data = request.form
		return render_template('result.html', data = data)
	#if no POST method, return user home, should be error message in real life
	return render_template('index.html')

@app.route('/contacts/<string:name>', methods=['GET'])
def returnOne(name):
	findContacts = [contact for contact in contacts if contact['name'] == name]
	return '''
	<li>name : {}</li>
	<li>address : {}</li>
	<li>city : {}</li>
	<li>state : {}</li>'''.format(name, address, city, state)

@app.route('/contacts/<int:id>', methods=['POST'])
def update_contact(id):
		return 'Updating...'

@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
	return 'Deleting...'


if __name__ == '__main__':
	app.run(debug=True, port=5000)