from app.extensions import db


class AdministrasiModel(db.Model):
    __tablename__ = 'administrasi'
    
    id = db.Column(db.Integer, primary_key=True)
    nama_pengelola = db.Column(db.String(100), nullable=False)
    kontak = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nama_pengelola": self.nama_pengelola,
            "kontak": self.kontak
        }