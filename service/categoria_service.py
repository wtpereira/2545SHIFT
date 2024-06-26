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

        input('\nPressione uma tecla para continuar...\n')

    def adicionar(self):
        print('Adicionando categoria...')
        try:
            nome = input('Digite o nome da categoria: ')
            nova_categoria = Categoria(nome)
            self.__categoria_dao.adicionar(nova_categoria)
            print('\nCategoria adicionada com sucesso!\n')
        except Exception as e:
            print(f'Erro ao adicionar categoria: {e}')

        input('\nPressione uma tecla para continuar...\n')

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

        input('\nPressione uma tecla para continuar...\n')

    def mostrar_por_id(self):
        print('Categoria por Id...')
        try:
            id = int(input('Digite o Id da categoria para buscar: '))
            cat = self.__categoria_dao.buscar_por_id(id)

            if cat is None:
                print('\nCategoria não encontrada\n')
            else:
                print(cat)
        except Exception as e:
            print(f'Erro ao exibir categoria: {e}')

        input('\nPressione uma tecla para continuar...\n')

    def importar_csv(self):
        print('Método ainda não implementado.')

    def importar_json(self):
        print('Método não implementado.')

    def exportar_json(self):
        print('Método não implementado.')
