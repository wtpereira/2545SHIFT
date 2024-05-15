import csv
from pathlib import Path

from model.editora import Editora


def caminho_completo(nome_arquivo_csv):
    return f'{str(Path().absolute())}/{nome_arquivo_csv}.csv'


def ler_csv_e_gera_uma_lista_de_editoras(nome_arquivo_csv) -> list[Editora]:
    with open(caminho_completo(nome_arquivo_csv)) as arquivo_csv:
        csv_reader = csv.DictReader(arquivo_csv, delimiter=',')
        lista_editoras = list()
        for dicionario in csv_reader:
            editora = Editora(dicionario['nome'], dicionario['endereco'], dicionario['telefone'])
            lista_editoras.append(editora)

        return lista_editoras
