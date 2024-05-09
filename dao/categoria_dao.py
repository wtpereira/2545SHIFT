from database.conexao_factory import ConexaoFactory
from model.categoria import Categoria


class CategoriaDAO:
    def __init__(self) -> None:
        self.__conexao_factory = ConexaoFactory()

    def listar(self) -> list[Categoria]:
        categorias = list()

        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT id, nome FROM categorias')
        resultados = cursor.fetchall()
        for resultado in resultados:
            cat = Categoria(resultado[1])
            cat.id = resultado[0]
            categorias.append(cat)

        cursor.close()
        conexao.close()

        return categorias

    def adicionar(self, categoria: Categoria) -> None:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(f'INSERT INTO categorias (nome) VALUES ({categoria.nome})')
        conexao.commit()
        cursor.close()
        conexao.close()

    def remover(self, categoria_id: int) -> bool:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(f'DELETE FROM categorias WHERE id = {categoria_id}')
        categorias_removidas = cursor.rowcount
        conexao.commit()
        cursor.close()
        conexao.close()

        if categorias_removidas == 0:
            return False

        return True

    def buscar_por_id(self, categora_id) -> Categoria:
        cat = None
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(f'SELECT id, nome FROM categorias where id = {categora_id}')
        resultado = cursor.fetchone()
        if resultado:
            cat = Categoria(resultado[1])
            cat.id = resultado[0]

        cursor.close()
        conexao.close()

        return cat

    def ultimo_id(self) -> int:
        index = len(self.__categorias) - 1
        if index == -1:
            id = 0
        else:
            id = self.__categorias[index].id

        return id
