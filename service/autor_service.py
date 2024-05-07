from service.menu_service import MenuService
from dao.autor_dao import AutorDAO
from model.autor import Autor


class AutorService(MenuService):
    def __init__(self):
        self.__autor_dao: AutorDAO = AutorDAO()

    @property
    def autor_dao(self) -> AutorDAO:
        return self.__autor_dao

    def listar(self):
        print('\nListando autores...')

        try:
            autores = self.__autor_dao.listar()
            if len(autores) == 0:
                print('Nenhum autor encontrado!')

            for autor in autores:
                print(autor)
        except Exception as e:
            print(f'Erro ao exibir os autores! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def adicionar(self):
        print('\nAdicionando autor...')

        try:
            id = self.__autor_dao.ultimo_id() + 1
            nome = input('Digite o nome do autor: ')
            email = input('Digite o email do autor: ')
            telefone = input('Digite o telefone do autor: ')
            bio = input('Digite uma bio reduzida do autor: ')
            novo_autor = Autor(id, nome, email, telefone, bio)
            self.__autor_dao.adicionar(novo_autor)
            print('Autor adicionado com sucesso!')
        except Exception as e:
            print(f'Erro ao inserir autor! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def remover(self):
        print('\nRemovendo autor...')

        try:
            autor_id = int(input('Digite o ID do autor para excluir: '))
            if (self.__autor_dao.remover(autor_id)):
                print('Autor excluído com sucesso!')
            else:
                print('Autor não encontrado!')
        except Exception as e:
            print(f'Erro ao excluir autor! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def mostrar_por_id(self):
        print('\nAutor por Id...')

        try:
            id = int(input('Digite o Id do autor para buscar: '))
            aut = self.__autor_dao.buscar_por_id(id)

            if (aut == None):
                print('Autor não encontrado!')
            else:
                print(f'Id: {aut.id} | Autor: {aut.nome} | Email: {aut.email} | Telefone: {aut.telefone} | Bio: {aut.bio}')
        except Exception as e:
            print(f'Erro ao exibir autor! - {e}')
            return

        input('Pressione uma tecla para continuar...')
