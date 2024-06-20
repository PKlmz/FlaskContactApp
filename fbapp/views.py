from flask import Flask, render_template, request

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    email = request.form.get('email')
    gender = request.form.get('gender')
    issue = request.form.get('issue')
    subject = request.form.get('subject')

    print("First Name:", firstname)
    print("Last name:", lastname)
    print("Email:", email)
    print("Gender:", gender)
    print("Issue:", issue)
    print("Subject:", subject)

    return "Form successfully submitted!"

#if __name__ == "__main__":
#    app.run()