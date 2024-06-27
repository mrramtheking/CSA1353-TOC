from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text_to_translate = request.form['text_to_translate']
        translator = Translator()
        translated_text = translator.translate(text_to_translate).text
        return render_template('index.html', translated_text=translated_text)
    return render_template('index.html', translated_text=None)

if __name__ == '__main__':
    app.run(debug=True)
