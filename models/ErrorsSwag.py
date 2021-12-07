from config.database import Database


class SwagBot:
    def __init__(self):
        self.db = Database()
        self.collection_name = 'swag-bot-errors'

    def create(self, data):
        res = self.db.insert(data, self.collection_name)
        return res

    def findAll(self, data, sort=None):
        return self.db.find(data, self.collection_name, None, sort)

    def find_by_id(self, _id):
        return self.db.find_by_id(_id, self.collection_name)

    def update(self, _id, data):
        return self.db.update(_id, data, self.collection_name)

    def upsert(self, _id, user):
        return self.db.upsert(_id, user, self.collection_name)

    def push(self, criteria, upd):
        return self.db.push(criteria, upd, self.collection_name)

    def delete(self, _id):
        return self.db.delete(_id, self.collection_name)

    def count(self):
        return self.db.count(self.collection_name)