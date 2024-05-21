from database.client_factory import ClientFactory
from model.box import Box
from bson.objectid import ObjectId


class BoxDAO:
    def __init__(self) -> None:
        self.__client = ClientFactory()

    def listar(self) -> list[Box]:
        boxes = list()
        client = self.__client.get_client()
        db = client.livraria  # use livraria
        for documento in db.box.find():
            box = Box(documento['nome'], documento['livros'])
            box.id = documento['_id']
            boxes.append(box)

        client.close()

        return boxes

    def adicionar(self, box: Box) -> None:
        client = self.__client.get_client()
        db = client.livraria  # use livraria
        result = db.box.insert_one(box)
        print(f'Resultado do insert: {result}')
        client.close()

    def remover(self, box_id: ObjectId) -> bool:
        client = self.__client.get_client()
        db = client.livraria  # use livraria
        result = db.box.delete_one({'_id': box_id})
        if result.deleted_count:
            return True

        return False
