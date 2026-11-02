from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from app.repositories.ppkl_repo import LahanRepository
from app.services.ppkl_services import LahanService
from app.utils.response_helper import error_response, fail_response, success_response

ppkl_bp = Blueprint('ppkl_v1', __name__, url_prefix='/api/v1/lahans')
service = LahanService(LahanRepository())

@ppkl_bp.route('/<int:lahan_id>', methods=['GET'])
def get_lahan_by_id(lahan_id):
    response, status_code = service.get_lahan_by_id(lahan_id)
    return jsonify(response), status_code

@ppkl_bp.route('', methods=['GET'])
def get_lahans():
    try:
        data, code = service.fetch_all()
        return success_response(data={"lahans": data}, code=code)
    except SQLAlchemyError as e:
        return error_response(str(e))

@ppkl_bp.route('', methods=['POST'])
def create_lahan():
    if not request.is_json:
        return fail_response({"content_type": "Header harus application/json"}, 400)
    body = request.get_json()
    res, code = service.add_lahan(body)
    if code == 400:
        return fail_response(res, 400)
    return success_response(data={"lahan": res}, message="Lahan berhasil disimpan", code=201)