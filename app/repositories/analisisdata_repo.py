from app import db
from app.models.analisisdata_model import TanamanModel


class TanamanRepository:
    def get_all(self):
        return TanamanModel.query.all()

    def create(self, data):
        try:
            new_tanaman = TanamanModel(
                lahan_id=data.get("lahan_id"),
                nama_tanaman=data.get("nama_tanaman"),
                status_pertumbuhan=data.get("status_pertumbuhan")
            )
            db.session.add(new_tanaman)
            db.session.commit()
            return new_tanaman
        except Exception:
            db.session.rollback()
            raise