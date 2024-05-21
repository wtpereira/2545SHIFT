class Editora:

    def __init__(self, nome: str, endereco: str, telefone: str):
        self.__id: int = 0
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def __str__(self) -> str:
        return f'{self.id} | {self.nome} | {self.endereco} | {self.telefone}'

    def __repr__(self) -> str:
        return f"{{ 'nome': {self.nome} }}"

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome.strip().title()

    @property
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    def as_dict(self) -> dict:
        return {
            'id': self.id,
            'nome': self.nome,
            'endereco': self.endereco,
            'telefone': self.telefone
        }
