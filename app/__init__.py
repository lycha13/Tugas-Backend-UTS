from flask import Flask

from app.extensions import db

from app.models.analisisdata_model import TanamanModel
from app.models.ppkl_model import LahanModel

from app.routes.ppkl_routes import ppkl_bp


def create_app():
    app = Flask(__name__)
    
    # Konfigurasi database MySQL Anda di sini (atau di config.py)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/db_lahan_tanaman'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inisialisasi db dengan app
    db.init_app(app)

    # Daftarkan blueprint
    app.register_blueprint(ppkl_bp)

    return app