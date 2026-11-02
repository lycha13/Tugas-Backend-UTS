class AdministrasiService:
    def __init__(self, repo):
        self.repo = repo

    def fetch_all(self):
        admins = self.repo.get_all()
        return [a.to_dict() for a in admins], 200

    def add_admin(self, data):
        if not data.get("nama_pengelola"):
            return {"nama_pengelola": "Field nama_pengelola wajib diisi"}, 400
        created = self.repo.create(data)
        return created.to_dict(), 201