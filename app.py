from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data for now
resources = []

@app.route('/')
def home():
    return render_template('index.html', resources=resources)

@app.route("/igcse")
def igcse():
    return render_template('igcse.html', resources=resources)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        link = request.form['link']
        resources.append({'title': title, 'description': description, 'link': link})
        return render_template('index.html', resources=resources)
    return render_template('add.html')

if __name__ == '__main__':
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

