from flask import Blueprint, jsonify

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/hello', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})
