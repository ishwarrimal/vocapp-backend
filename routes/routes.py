from flask import Blueprint, request, redirect, url_for

main_routes_bp = Blueprint('main_routes', __name__)

@main_routes_bp.route('/')
def index():
    return 'Welcome to the main page!'

@main_routes_bp.route('/word-list/<int:uid>')
def getWordList(uid):
    # uid = request.args.get('uid', type=int)
    return 'Your uid is %d ' %uid




# Below is sample code to do dynamic redirection
# @main_routes_bp.route('/admin')
# def hello_admin():
#    return 'Hello Admin'

# @main_routes_bp.route('/user/<name>')
# def redirect_user(name):
#     if(name == 'admin'):
#         return redirect(url_for('main_routes.hello_admin'))
#     else:
#         return redirect(url_for('main_routes.index'))