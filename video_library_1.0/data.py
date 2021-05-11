import json

class Videos:
    def __init__(self):
        try:
            with open("videos.json", "r") as f:
                self.videos = json.load(f)
        except FileNotFoundError:
            self.videos = []

    def all(self):
        return self.videos

    def get(self, id):
        return self.videos[id]

    def create(self, data):
        data.pop('csrf_token')
        self.videos.append(data)

    def save_all(self):
        with open("videos.json", "w") as f:
            json.dump(self.videos, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.videos[id] = data
        self.save_all()

    def delete(self, data):
        data.pop('csrf_token')
        self.videos.remove(data)



videos = Videos()