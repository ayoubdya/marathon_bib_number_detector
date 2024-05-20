import pickle


class DataManager:
    def __init__(self, path):
        self.path = path

    def save(self, obj):
        with open(self.path, 'wb') as f:
            pickle.dump(obj, f)

    def load(self):
        with open(self.path, 'rb') as f:
            return pickle.load(f)

    def update(self, data):
        obj = self.load()
        for key, array in data.items():
            if obj.get(key):
                obj[key].extend(array)
            else:
                obj[key] = array
        self.save(obj)
