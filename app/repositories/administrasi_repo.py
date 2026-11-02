from app import db
from app.models.administrasi_model import AdministrasiModel


class AdministrasiRepository:
    def get_all(self):
        return AdministrasiModel.query.all()

    def create(self, data):
        try:
            new_admin = AdministrasiModel(
                nama_pengelola=data.get("nama_pengelola"),
                kontak=data.get("kontak")
            )
            db.session.add(new_admin)
            db.session.commit()
            return new_admin
        except Exception:
            db.session.rollback()
            raise