from flask import Blueprint, request, jsonify

main_routes_bp = Blueprint('main_routes', __name__)

@main_routes_bp.route('/')
def index():
    return 'Welcome to the main page!'

@main_routes_bp.route('/word-list/<int:uid>')
def getWordList(uid):
    # uid = request.args.get('uid', type=int)
    return 'Your uid is %d ' %uid
