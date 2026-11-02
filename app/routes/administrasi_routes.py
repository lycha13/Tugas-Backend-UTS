from flask import Blueprint, request
from sqlalchemy.exc import SQLAlchemyError

from app.repositories.administrasi_repo import AdministrasiRepository
from app.services.administrasi_services import AdministrasiService
from app.utils.response_helper import error_response, fail_response, success_response

admin_bp = Blueprint('admin_v1', __name__, url_prefix='/api/v1/administrasi')
service = AdministrasiService(AdministrasiRepository())

@admin_bp.route('', methods=['GET'])
def get_admins():
    try:
        data, code = service.fetch_all()
        return success_response(data={"administrasi": data}, code=code)
    except SQLAlchemyError as e:
        return error_response(str(e))

@admin_bp.route('', methods=['POST'])
def create_admin():
    if not request.is_json:
        return fail_response({"content_type": "Header harus application/json"}, 400)
    body = request.get_json()
    res, code = service.add_admin(body)
    if code == 400:
        return fail_response(res, 400)
    return success_response(data={"administrasi": res}, message="Data administrasi disimpan", code=201)