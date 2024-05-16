from database.conexao_factory import ConexaoFactory
from model.autor import Autor


class AutorDAO:

    def __init__(self):
        self.__conexao_factory = ConexaoFactory()

    def listar(self) -> list[Autor]:
        autores = list()
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, email, telefone, bio FROM autores")
        resultados = cursor.fetchall()
        for resultado in resultados:
            autor = Autor(resultado[1], resultado[2], resultado[3], resultado[4])
            autor.id = resultado[0]
            autores.append(autor)
        cursor.close()
        conexao.close()
        return autores

    def adicionar(self, autor: Autor) -> None:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO autores (nome, email, telefone, bio) VALUES (%(nome)s, %(email)s, %(telefone)s, %(biografia)s)",
            ({'nome': autor.nome, 'email': autor.email, 'telefone': autor.telefone, 'biografia': autor.bio}))
        conexao.commit()
        cursor.close()
        conexao.close()

    def remover(self, autor_id: int) -> bool:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM autores WHERE id = {autor_id}")
        autores_removidos = cursor.rowcount
        conexao.commit()
        cursor.close()
        conexao.close()

        if autores_removidos == 0:
            return False

        return True

    def buscar_por_id(self, autor_id) -> Autor:
        aut = None
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT id, nome, email, telefone, bio FROM autores WHERE id = {autor_id}")
        resultado = cursor.fetchone()
        if resultado:
            aut = Autor(resultado[1], resultado[2], resultado[3], resultado[4])
            aut.id = resultado[0]

        cursor.close()
        conexao.close()

        return aut

    def adicionar_muitos(self, lista_autores: list):
        for autor in lista_autores:
            self.adicionar(autor)
