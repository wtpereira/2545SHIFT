import psycopg2


class ConexaoFactory:
    def get_conexao(self):
        return psycopg2.connect(host='ep-nameless-recipe-a4e8ctcf.us-east-1.aws.neon.tech', database='livraria', user='livraria_owner', password='f10JxmXRthpu')
