from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask (__name__)
cors = CORS (app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route ('/', methods = ['POST'])
@cross_origin ()
def genericMethod ():
    firstname = request.json ['firstname']
    print (firstname)
    return jsonify ({'output' : firstname})
    
if __name__ == '__main__':
    app.run (debug=True)