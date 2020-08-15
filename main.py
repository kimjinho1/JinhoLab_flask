from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/dog-cat')
def dog_cat():
    return render_template('dog-cat.html')

@app.route('/animal-face')
def animal_face():
    return render_template('animal-face.html')

if __name__ == '__main__':
    app.run()