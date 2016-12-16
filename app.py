from flask import Flask, render_template, session, request, redirect, url_for, escape
import json

app = Flask(__name__)


@app.route('/')
def index():
    # ша
    # sessions['lang'] = 'uk'
    return render_template('index.html', lang='ua')


@app.route('/poll', methods=['POST', 'GET'])
def poll():
    if request.method == 'POST':
        if 'lang' in request.form:
            session['lang'] = request.form['lang']

        if 'question-id' in request.form:
            session['question-id'] = request.form['question-id']
        else:
            return redirect('/')

    if 'lang' not in session:
        return redirect('/')

    id = int(session['question-id'])

    with open('questions/' + session['lang'] + '.json', encoding='UTF-8') as data:
        questions = json.load(data)

    if 'next' not in questions['questions'][id]:
        id += 1
    question = questions['questions'][id]
    translation = questions['translation']

    print(question)
    if question['type'] == 'quiz':
        return render_template('quiz.html', id=id, question=question, translation=translation)
    elif question['type'] == 'open':
        return render_template('open.html', id=id, question=question, translation=translation)
    elif question['type'] == 'quiz-or-open':
        return render_template('quiz-or-open.html', id=id, question=question, translation=translation)
    else:
        print(question['type'])
        return 'Error 404'

if __name__ == '__main__':
    app.secret_key = 'f04c8f9e2328040b2716dd6a294fc122b8c478b524688dbd'
    app.run(debug=True)
