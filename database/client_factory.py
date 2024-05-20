from os import getenv
from dotenv import load_dotenv

from pymongo import MongoClient
from pymongo.server_api import ServerApi


load_dotenv()  # take environment variables from .env.


class ClientFactory:
    def get_client(self):
        return MongoClient(getenv('MONGODB_CONNECTION_STRING'), server_api=ServerApi('1'))


if __name__ == '__main__':
    client = MongoClient(getenv('MONGODB_CONNECTION_STRING'), server_api=ServerApi('1'))

    try:
        print(client.admin.command('ping'))
        print('Conectado ao banco de dados!')
    except Exception as e:
        print(e)
