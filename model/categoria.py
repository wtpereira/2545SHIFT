class Categoria:
    def __init__(self, nome: str) -> None:
        self.__id: int = 0
        self.nome = nome

    def __str__(self) -> str:
        return f'{self.id} | {self.nome}'

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

    def as_dict(self) -> dict:
        return {
            'id': self.id,
            'nome': self.nome
        }
