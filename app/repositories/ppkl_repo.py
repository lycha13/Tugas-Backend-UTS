from app import db
from app.models.ppkl_model import LahanModel


class LahanRepository:
    def get_all(self):
        return LahanModel.query.all()

    def get_by_id(self, lahan_id):
        return LahanModel.query.get(lahan_id)

    def create(self, data):
        try:
            new_lahan = LahanModel(
                name=data.get("name"),
                location=data.get("location"),
                desc=data.get("desc")
            )
            db.session.add(new_lahan)
            db.session.commit()
            return new_lahan
        except Exception:
            db.session.rollback()
            raise

    def update(self, lahan, data):
        try:
            lahan.name = data.get("name", lahan.name)
            lahan.location = data.get("location", lahan.location)
            lahan.desc = data.get("desc", lahan.desc)
            db.session.commit()
            return lahan
        except Exception:
            db.session.rollback()
            raise

    def delete(self, lahan):
        try:
            db.session.delete(lahan)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise