import csv
from pathlib import Path

from model.autor import Autor


def caminho_completo(nome_arquivo_csv):
    return f'{str(Path().absolute())}/{nome_arquivo_csv}.csv'


def ler_csv_e_gera_uma_lista_de_autores(nome_arquivo_csv) -> list[Autor]:
    with open(caminho_completo(nome_arquivo_csv)) as arquivo_csv:
        csv_reader = csv.DictReader(arquivo_csv, delimiter=',')
        lista_editoras = list()
        for dicionario in csv_reader:
            editora = Autor(dicionario['nome'], dicionario['email'], dicionario['telefone'], dicionario['biografia'])
            lista_editoras.append(editora)

        return lista_editoras


def ler_csv() -> None:
    arquivo_csv = open('editoras.csv')
    csv_reader = csv.reader(arquivo_csv, delimiter=',')
    for linha in csv_reader:
        print(linha)

    arquivo_csv.close()
