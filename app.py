from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    regexPattern = request.form.get('regex_pattern')
    testingText = request.form.get('testing_text')

    matches = re.findall(regexPattern, testingText)
    highlightedText = re.sub(f'({regexPattern})', r'<mark>\1</mark>', testingText)

    return render_template('result.html', matches=matches, highlightedText=highlightedText)

@app.route('/validateEmail', methods=['POST'])
def validateEmail():
    email = request.form['email']
    if re.match(r'^[\w\.-]+@[\w\.-]+$', email):
        return render_template('emailValidation.html', valid=True, email=email)
    else:
        return render_template('emailValidation.html', valid=False, email=email)

if __name__ == '__main__':
    app.run(debug=True)
