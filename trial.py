from flask import Flask, render_template, send_from_directory, request, jsonify
from flipkart_scraper import flipkart
app = Flask(__name__)

@app.route('/', methods= ["GET", "POST"])
def homepage():
    if request.method == 'POST':
        story = request.form['input_text']
        if story:
            result = flipkart(story)
            return jsonify(result=result)
        else:
            return jsonify(result='Input needed')

    return render_template('webpage.html')

if __name__ == "__main__":
    app.debug=True
    app.run()