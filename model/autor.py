class Autor:

    def __init__(self, nome: str, email: str, telefone: str, bio: str):
        self.__id: int = 0
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.bio = bio

    def __str__(self) -> str:
        return f'{self.id} | {self.nome} | {self.email} | {self.telefone} | {self.bio}'

    def __repr__(self) -> str:
        return f"{{'nome': {self.nome} }}"

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
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email.strip().lower()

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone

    @property
    def bio(self) -> str:
        return self.__bio

    @bio.setter
    def bio(self, bio: str):
        self.__bio = bio

    def as_dict(self) -> dict:
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone,
            'bio': self.bio
        }
