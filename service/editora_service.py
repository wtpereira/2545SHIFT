from service.menu_service import MenuService
from dao.editora_dao import EditoraDAO
from model.editora import Editora
from utils import editoras_csv, editoras_json


class EditoraService(MenuService):
    def __init__(self):
        self.__editora_dao: EditoraDAO = EditoraDAO()

    @property
    def editora_dao(self) -> EditoraDAO:
        return self.__editora_dao

    def listar(self):
        print('\nListando editoras...')

        try:
            editoras = self.__editora_dao.listar()
            if len(editoras) == 0:
                print('Nenhuma editora encontrada!')

            for editora in editoras:
                print(editora)
        except Exception as e:
            print(f'Erro ao exibir as editoras! - {e}')
            return

        input('\nPressione uma tecla para continuar...\n')

    def adicionar(self):
        print('\nAdicionando editora...')

        try:
            nome = input('Digite o nome da editora: ')
            endereco = input('Digite o endereço da editora: ')
            telefone = input('Digite o telefone da editora: ')
            nova_editora = Editora(nome, endereco, telefone)

            self.__editora_dao.adicionar(nova_editora)
            print('Editora adicionada com sucesso!')
        except Exception as e:
            print(f'Erro ao inserir editora! - {e}')
            return

        input('\nPressione uma tecla para continuar...\n')

    def remover(self):
        print('\nRemovendo editora...')

        try:
            editora_id = int(input('Digite o ID da excluir para excluir: '))
            if (self.__editora_dao.remover(editora_id)):
                print('Editora excluída com sucesso!')
            else:
                print('Editora não encontrada!')
        except Exception as e:
            print(f'Erro ao excluir editora! - {e}')
            return

        input('\nPressione uma tecla para continuar...\n')

    def mostrar_por_id(self):
        print('\Editora por Id...')

        try:
            id = int(input('Digite o Id da editora para buscar: '))
            edt = self.__editora_dao.buscar_por_id(id)

            if edt is None:
                print('Editora não encontrada!')
            else:
                print(f'{edt.id} | {edt.nome} | {edt.endereco} | {edt.telefone}')
        except Exception as e:
            print(f'Erro ao exibir editora! - {e}')
            return

        input('\nPressione uma tecla para continuar...\n')

    def importar_csv(self):
        print('Importar editoras CSV...')
        try:
            nome_arquivo = input('Digite o nome do arquivo CSV (precisa estar na raiz do projeto): ')
            lista_dict_editoras = editoras_csv.ler_csv_e_gera_uma_lista_de_editoras(nome_arquivo)
            self.__editora_dao.adicionar_muitos(lista_dict_editoras)
            print('Editoras do CSV importadas com sucesso!')
        except Exception as e:
            print(f'Erro ao importar dados do arquivo CSV: {e}')
            return

        input('\nPressione uma tecla para continuar...\n')

    def importar_json(self):
        print('Importar editoras JSON...')
        try:
            nome_arquivo = input('Digite o nome do arquivo JSON (precisa estar na raiz do projeto): ')
            lista_dict_editoras = editoras_json.ler_json_e_gera_uma_lista_de_editoras(nome_arquivo)
            self.__editora_dao.adicionar_muitos(lista_dict_editoras)
            print('Editoras do JSON importadas com sucesso!')
        except Exception as e:
            print(f'Erro ao importar dados do arquivo JSON: {e}')
            return

        input('\nPressione uma tecla para continuar...\n')

    def exportar_json(self):
        print('Exportar editoras JSON...')
        try:
            nome_arquivo = input('Digite o nome para o novo arquivo JSON (será gerado na pasta raiz do projeto): ')
            lista_de_editoras = self.__editora_dao.listar()
            editoras_json.criando_json_usando_lista_de_editoras(lista_de_editoras, nome_arquivo)
            print('JSON de editoras gerado com sucesso!')
        except Exception as e:
            print(f'Erro ao exportar arquivo JSON: {e}')
            return

        input('\nPressione uma tecla para continuar...\n')
