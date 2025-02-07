import json


class EqualityMixin:
    def __eq__(self, other):
        return type(self) == type(other) and self.__dict__ == other.__dict__


class SerializeMixin:
    #  принимает JSON и создает новый объект из него
    @classmethod
    def deserialize(cls, serialized):
        obj_data = json.loads(serialized)
        # Создаем новый объект текущего класса на основе данных из словаря
        return cls(**obj_data)

    # возвращает сериализованное представление объекта в JSON
    def serialize(self):
        return json.dumps(self.__dict__)
