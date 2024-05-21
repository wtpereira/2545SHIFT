from bson.objectid import ObjectId

from .menu_service import MenuService
from dao.autor_dao import AutorDAO
from dao.categoria_dao import CategoriaDAO
from dao.editora_dao import EditoraDAO
from dao.livro_dao import LivroDAO
from dao.box_dao import BoxDAO
from model.box import Box

from service.livro_service import LivroService


class BoxService(MenuService):
    def __init__(self) -> None:
        self.__box_dao = BoxDAO()
        self.__livro_dao: LivroDAO = LivroDAO()
        self.__categoria_dao: CategoriaDAO = CategoriaDAO()
        self.__editora_dao: EditoraDAO = EditoraDAO()
        self.__autor_dao: AutorDAO = AutorDAO()
        self.__livro_service: LivroService = LivroService(self.__categoria_dao, self.__editora_dao, self.__autor_dao)

    def listar(self):
        print('\nListando boxes de livros...')

        try:
            boxes = self.__box_dao.listar()
            if len(boxes) == 0:
                print('Nenhum box de livro encontrado.')

            for box in boxes:
                print(box)
        except Exception as e:
            print(f'Erro ao exibir os boxes: {e}')

        input('Pressione uma tecla para continuar...')

    def adicionar(self):
        print('\nAdicionando um box de livros...')

        try:
            nome = input('Digite o nome do box de livros: ')
            print('Livros disponíveis: ')
            self.__livro_service.listar()

            lista_livros = list()
            id_livro = input('Digite o ID do livro que você quer adicionar:')
            while id_livro:
                livro = self.__livro_dao.buscar_por_id(id_livro)
                lista_livros.append(livro.as_dict())
                id_livro = input('Digite o ID do livro que você quer adicionar:')

            novo_box = Box(nome=nome, livros=lista_livros)
            self.__box_dao.adicionar(novo_box.as_dict())
        except Exception as e:
            print(f'Erro ao inserir box de livros: {e}')
            return

        input('Pressione uma tecla para continuar...')

    def remover(self):
        print('\nRemovendo o box service...')

        try:
            box_id = input('Digite o ID do box de livros para excluir: ')
            if self.__box_dao.remover(ObjectId(box_id)):
                print('Box excluído com sucesso!')
            else:
                print('Box não encontrado!')

        except Exception as e:
            print(f'Erro ao remover o box: {e}')

        input('Pressione uma tecla para continuar...')
