import os


class Config:
    # Konfigurasi dasar Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key-banyuwangi'
    
    # Konfigurasi Database MySQL menggunakan PyMySQL
    # Format: mysql+pymysql://username:password@host:port/nama_database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:@localhost:3306/db_lahan_tanaman'
    
    # Menonaktifkan tracking modifikasi untuk menghemat memori
    SQLALCHEMY_TRACK_MODIFICATIONS = False