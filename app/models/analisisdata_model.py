from app.extensions import db


class TanamanModel(db.Model):
    __tablename__ = 'tanaman'
    
    id = db.Column(db.Integer, primary_key=True)
    lahan_id = db.Column(db.Integer, db.ForeignKey('lahan.id', ondelete='CASCADE'), nullable=False)
    nama_tanaman = db.Column(db.String(100), nullable=False)
    status_pertumbuhan = db.Column(db.String(50), nullable=False) # Contoh: Sehat, Layu, Panen

    def to_dict(self):
        return {
            "id": self.id,
            "lahan_id": self.lahan_id,
            "nama_tanaman": self.nama_tanaman,
            "status_pertumbuhan": self.status_pertumbuhan
        }