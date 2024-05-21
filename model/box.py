class Box:
    def __init__(self, nome: str, livros: dict = None) -> None:
        self.__id: int = 0
        self.__nome: str = nome
        self.__livros: dict = livros

    def __str__(self) -> str:
        return f'{self.__id} | {self.__nome} | {self.__livros}'

    def __repr__(self) -> str:
        return f"{{'nome': {self.nome}, 'livros': {self.livros} }}"

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
        self.__nome = nome

    @property
    def livros(self) -> dict:
        return self.__livros

    @livros.setter
    def livros(self, livros: dict):
        self.__livros = livros

    def as_dict(self) -> dict:
        return {'nome': self.nome, 'livros': self.livros}
