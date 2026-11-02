from app.extensions import db


class LahanModel(db.Model):
    __tablename__ = 'lahan'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    desc = db.Column(db.Text, nullable=True)
    
    tanamans = db.relationship('TanamanModel', backref='lahan', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "desc": self.desc,
            "tanamans": [t.to_dict() for t in self.tanamans]
        }