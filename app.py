from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

messages = []  # Temporary storage (clears when you restart the server)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form.get('message')
        if text:
            messages.append(text)
        return redirect(url_for('home'))
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
