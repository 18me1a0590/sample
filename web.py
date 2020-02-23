from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('clg.html')

@app.route('/about.html')
def index1():
    return render_template('about.html')

@app.route('/collaboration.html')
def index2():
    return render_template('collaboration.html')

@app.route('/rcee.html')
def index3():
    return render_template('rcee.html')

@app.route('/clg.html')
def index4():
    return render_template('clg.html')



if __name__ == '__main__' :
    app.run(debug=True)
