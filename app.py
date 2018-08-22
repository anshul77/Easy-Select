from flask import Flask, render_template, send_from_directory, request
from flipkart_scraper import flipkart
from flask import jsonify
from amazon_scraper import amazon
app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    return render_template("webpage.html")


@app.route("/templates",methods=["GET","POST"])
def reg():
        text = request.form['input_text']
        print('query -')
        print(text)
        flip = flipkart(text)
        amaz = amazon(text)
        #return jsonify(titles)
        #titleq="abchdsjchsjdhkjdchdsjhkxckdhckjdvjidscjdhfureh"
        
        # print("flipkart")
        # print(flip[0])
        return render_template("price.html",titlef=flip,titlea=amaz)
        
        
        #return jsonify(titles,titlea)
        #titleq="abchdsjchsjdhkjdchdsjhkxckdhckjdvjidscjdhfureh"
        #return render_template("webpage.html",title=titleq)
@app.route('/templates/<k>',methods=["GET","POST"])
def reg2(k):
    print(k)
if __name__ == '__main__':
    try:
        app.run('localhost', port = 5000, debug = True, use_reloader = False)
    except Exception as e:
        print (e)
    