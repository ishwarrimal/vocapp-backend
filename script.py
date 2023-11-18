from flask import Flask
from routes.routes import main_routes_bp


app = Flask(__name__)

app.register_blueprint(main_routes_bp)

if __name__ == '__main__':
   app.run(port=3000, debug= True)