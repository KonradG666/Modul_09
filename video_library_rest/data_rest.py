import json

class Videos:
    def __init__(self):
        try:
            with open("videos1.json", "r") as f:
                self.videos = json.load(f)
        except FileNotFoundError:
            self.videos = []

    def all(self):
        return self.videos

    def get(self, id):
        video = [video for video in self.all() if video['id'] == id]
        if video:
            return video[0]
        return []

    def create(self, data):
        self.videos.append(data)
        self.save_all()

    def save_all(self):
        with open("videos1.json", "w") as f:
            json.dump(self.videos, f)

    def update(self, id, data):
        video = self.get(id)
        if video:
            index = self.videos.index(video)
            self.videos[index] = data
            self.save_all()
            return True
        return False


    def delete(self, id):
        video = self.get(id)
        if video:
            self.videos.remove(video)
            self.save_all()
            return True
        return False



videos = Videos()



