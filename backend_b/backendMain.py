from trail1_language import *
from trail2_emotion import *
from trail3_socialActivity import *
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
'''
@app.route("/trail1")
def trail1():
    return trail1()

@app.route("/trail2")
def trail2():
    return trail2()

@app.route("/trail3")
def trail3():
    return trail3()
'''
if __name__ == "__main__":
    app.run(host='172.26.128.11',port=8081)

'''
if __name__ == '__main__':
    trail1()
    trail2()
    trail3()
'''
