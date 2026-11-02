class LahanService:
    def __init__(self, repo):
        self.repo = repo

    def fetch_all(self):
        lahans = self.repo.get_all()
        return [l.to_dict() for l in lahans], 200

    def get_lahan_by_id(self, lahan_id):
        lahan = self.repo.get_by_id(lahan_id)

        if not lahan:
            return {"message": "Data lahan tidak ditemukan"}, 404

        return lahan.to_dict(), 200

    def add_lahan(self, data):
        errors = {}
        if not data:
            return {"body": "Payload kosong"}, 400

        if not data.get("name"):
            errors["name"] = "Field name wajib diisi"
        if not data.get("location"):
            errors["location"] = "Field location wajib diisi"

        if errors:
            return errors, 400

        created = self.repo.create(data)
        return created.to_dict(), 201