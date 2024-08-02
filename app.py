from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',title_data="FLASK 101")

@app.route('/about')
def about():
    return render_template('about.html', title_data="About Us")

@app.route('/contact')
def contact():
    return render_template('contact.html', title_data=["Contact Us","ERIC TUTORIAL"])









if __name__ == '__main__':
    app.run(debug=True)