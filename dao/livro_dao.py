from dao.autor_dao import AutorDAO
from dao.categoria_dao import CategoriaDAO
from dao.editora_dao import EditoraDAO
from database.conexao_factory import ConexaoFactory
from model.livro import Livro


class LivroDAO:
    def __init__(self) -> None:
        self.__conexao_factory = ConexaoFactory()
        self.__categoria_dao = CategoriaDAO()
        self.__editora_dao = EditoraDAO()
        self.__autor_dao = AutorDAO()

    def listar(self) -> list[Livro]:
        livros = list()
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, titulo, resumo, ano, paginas, isbn, categoria_id, editora_id, autor_id FROM livros")
        resultados = cursor.fetchall()
        for resultado in resultados:
            categoria = self.__categoria_dao.buscar_por_id(resultado[6])
            editora = self.__editora_dao.buscar_por_id(resultado[7])
            autor = self.__autor_dao.buscar_por_id(resultado[8])

            livro = Livro(resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], categoria, editora, autor)
            livro.id = resultado[0]

            livros.append(livro)

        cursor.close()
        conexao.close()

        return livros

    def adicionar(self, livro: Livro):
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO livros(titulo, resumo, ano, paginas, isbn, categoria_id, editora_id, autor_id) " \
            "VALUES (%(t)s, %(r)s, %(a)s, %(p)s, %(i)s, %(ci)s, %(ei)s, %(ai)s)",
            {'t': livro.titulo, 'r': livro.resumo, 'a': livro.ano, 'p': livro.paginas, 'i': livro.isbn,
             'ci': livro.categoria.id, 'ei': livro.editora.id, 'ai': livro.autor.id }
        )
        conexao.commit()
        cursor.close()
        conexao.close()

    def remover(self, livro_id: int) -> bool:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM livros WHERE id = {livro_id}")
        livros_removidos = cursor.rowcount
        conexao.commit()
        cursor.close()
        conexao.close()

        if livros_removidos:
            return True

        return False

    def buscar_por_id(self, livro_id) -> Livro:
        livro = None
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT id, titulo, resumo, ano, paginas, isbn, categoria_id, editora_id, autor_id FROM livros where id = {livro_id}")
        resultado = cursor.fetchone()
        if resultado:
            categoria = self.__categoria_dao.buscar_por_id(resultado[6])
            editora = self.__editora_dao.buscar_por_id(resultado[7])
            autor = self.__autor_dao.buscar_por_id(resultado[8])

            livro = Livro(resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], categoria, editora, autor)
            livro.id = resultado[0]

        cursor.close()
        conexao.close()

        return livro
