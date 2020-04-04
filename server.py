import json

from flask import Flask

app = Flask(__name__)

# Route to videos endpoint
@app.route('/videos')
def videos():
    # Load json data into file_data variable every time a request is made to this endpoint
    with open('./results-20191105-104506.json', 'r') as jsonfile:
        file_data = json.loads(jsonfile.read())
    # We can then find the data for the requested date and send it back as json
    return json.dumps(file_data)

if __name__ == '__main__':
    app.run(debug=True)





