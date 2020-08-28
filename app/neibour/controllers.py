from flask import (
    Blueprint,
    current_app,
    Flask,
    jsonify,
    abort,
    make_response,
    request
)
from sqlalchemy.exc import SQLAlchemyError

from .models import Neibour, db, NeibourSchema


module = Blueprint('neibour', __name__)
dot_schema = NeibourSchema()
dots_schema = NeibourSchema(many=True)


def log_error(*args, **kwargs):
    current_app.logger.error(*args, **kwargs)


@module.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@module.route('/neibour/api/dots', methods=['POST'])
def create_dot():
    dx = int(request.json["dx"])
    dy = int(request.json["dy"])
    echo = request.json["echo"]

    new_dot = Neibour(dx, dy, echo)

    db.session.add(new_dot)
    db.session.commit()

    return dot_schema.jsonify(new_dot), 201


@module.route('/neibour/api/dots', methods=['GET'])
def get_dots():
    all_dots = Neibour.query.all()
    result = dots_schema.dump(all_dots)
    return jsonify(result)


@module.route('/neibour/api/dots/<dot_id>', methods=['GET'])
def get_dot(dot_id):
    dot = Neibour.query.get(dot_id)
    return dot_schema.jsonify(dot)


@module.route('/neibour/api/dots/<dot_id>', methods=['PUT'])
def update_dot(dot_id):
    dot = Neibour.query.get(dot_id)
    x = request.json['dx']
    y = request.json['dy']
    echo = request.json['echo']
    dot.dx = x
    dot.dy = y
    dot.echo = echo
    db.session.commit()
    return dot_schema.jsonify(dot)


@module.route('/neibour/api/dots/<dot_id>', methods=['DELETE'])
def delete_dot(dot_id):
    dot = Neibour.query.get(dot_id)
    if dot is not None:
        db.session.delete(dot)
        db.session.commit()
        return dot_schema.jsonify({"Dot was deleted": True}), 201
    else:
        abort(
            404,
            "Dot no found"
        )
