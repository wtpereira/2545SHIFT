from service.menu_service import MenuService
from dao.categoria_dao import CategoriaDAO
from model.categoria import Categoria


class CategoriaService(MenuService):
    def __init__(self) -> None:
        self.__categoria_dao: CategoriaDAO = CategoriaDAO()

    @property
    def categoria_dao(self) -> CategoriaDAO:
        return self.__categoria_dao

    def listar(self):
        print('\nListando categorias...')
        try:
            categorias = self.__categoria_dao.listar()
            if len(categorias) == 0:
                print('\nNenhuma categoria encontrada!\n')
            else:
                for categoria in categorias:
                    print(categoria)
        except Exception as e:
            print(f'Erro ao exibir as categorias: {e}')

        input('Pressione uma tecla para continuar...')

    def adicionar(self):
        print('Adicionando categoria...')
        try:
            id = self.__categoria_dao.ultimo_id() + 1
            nome = input('Digite o nome da categora: ')
            nova_categoria = Categoria(id, nome)
            self.__categoria_dao.adicionar(nova_categoria)
            print('\nCategoria adicionada com sucesso!\n')
        except Exception as e:
            print(f'Erro ao adicionar categoria: {e}')

        input('Pressione uma tecla para continuar...')

    def remover(self):
        print('Removendo categoria...')

        try:
            categoria_id = int(input('Digite o ID da categoria para excluir: '))
            if self.__categoria_dao.remover(categoria_id):
                print('\nCategoria excluída com sucesso!\n')
            else:
                print('\nCategoria não encontrada!\n')
        except Exception as e:
            print(f'Erro ao remover categoria: {e}')

        input('Pressione uma tecla para continuar...')

    def mostrar_por_id(self):
        print('Categoria por Id...')
        try:
            id = int(input('Digite o Id da categoria para buscar: '))
            cat = self.__categoria_dao.buscar_por_id(id)

            if cat == None:
                print('\nCategoria não encontrada\n')
            else:
                print(f'Id: {cat.id} | Categoria: {cat.nome}')
        except Exception as e:
            print(f'Erro ao exibir categoria: {e}')

        input('Pressione uma tecla para continuar...')
