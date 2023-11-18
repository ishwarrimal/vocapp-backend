from flask import Flask
app = Flask(__name__)


@app.route('/hello/<name>')
def hello_world(name):
   return 'Hello %s!' %name

@app.route('/word-list/<int:uid>')
def get_words(uid):
   return 'Your uid is %d! ' %uid

if __name__ == '__main__':
   app.run(port=3000, debug= True)