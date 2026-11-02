from flask import Blueprint, request
from app.repositories.analisisdata_repo import TanamanRepository
from app.services.analisisdata_services import TanamanService
from app.utils.response_helper import success_response, fail_response, error_response

tanaman_bp = Blueprint('tanaman_v1', __name__, url_prefix='/api/v1/tanamans')
service = TanamanService(TanamanRepository())

@tanaman_bp.route('', methods=['GET'])
def get_tanamans():
    try:
        data, code = service.fetch_all()
        return success_response(data={"tanamans": data}, code=code)
    except Exception as e:
        return error_response(str(e))

@tanaman_bp.route('', methods=['POST'])
def create_tanaman():
    if not request.is_json:
        return fail_response({"content_type": "Header harus application/json"}, 400)
    body = request.get_json()
    res, code = service.add_tanaman(body)
    if code == 400:
        return fail_response(res, 400)
    return success_response(data={"tanaman": res}, message="Tanaman berhasil disimpan", code=201)