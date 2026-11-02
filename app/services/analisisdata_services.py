class TanamanService:
    def __init__(self, repo):
        self.repo = repo

    def fetch_all(self):
        tanamans = self.repo.get_all()
        return [t.to_dict() for t in tanamans], 200

    def add_tanaman(self, data):
        errors = {}
        if not data.get("lahan_id"):
            errors["lahan_id"] = "Field lahan_id wajib diisi"
        if not data.get("nama_tanaman"):
            errors["nama_tanaman"] = "Field nama_tanaman wajib diisi"
            
        if errors:
            return errors, 400

        created = self.repo.create(data)
        return created.to_dict(), 201