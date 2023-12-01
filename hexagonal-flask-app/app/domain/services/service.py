from app.domain.api.models import MyModel
from app.infrastructure.repository import MyModelRepository

class MyModelService:
    def __init__(self):
        self.repository = MyModelRepository()

    def create_my_model(self, data):
        my_model = MyModel(data)
        self.repository.save(my_model)
        return my_model

    def get_my_model(self, id):
        my_model = self.repository.get(id)
        return my_model

    def update_my_model(self, id, data):
        my_model = self.repository.get(id)
        my_model.update(data)
        self.repository.save(my_model)
        return my_model

    def delete_my_model(self, id):
        my_model = self.repository.get(id)
        self.repository.delete(my_model)