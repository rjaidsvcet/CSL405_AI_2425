from flask import Flask, render_template, request

app = Flask (__name__)

@app.route ('/loader')
def pageLoader ():
    return render_template ('index.html')

@app.route ('/', methods = ['GET'])
def genericMethod ():
    if request.method == 'GET':
        username = request.args ['username']
        password = request.args ['password']
        print (username, password)
        return 'Success'
    else:
        return render_template ('index.html')

@app.route ('/page', methods = ['POST'])
def basic ():
    if request.method == 'POST':
        username = request.form ['username']
        password = request.form ['password']
        print (username, password)
        return 'Success using post method'
    return render_template ('index.html')

if __name__ == '__main__':
    app.run (debug=True)