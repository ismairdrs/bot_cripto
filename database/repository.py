import os

import dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .entities import Cripto


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


BASE_DIR = os.path.dirname(os.path.realpath("__file__"))
dotenv.load_dotenv(os.path.join(BASE_DIR, ".env"))


class DBConnectionHandler:
    """sqlalchemy"""

    def __init__(self):
        self.__connection_string = "postgresql://myprojectuser:password@localhost:5432/botbtc"
        self.session = None

    def get_engine(self):
        """return connection engine"""
        return create_engine(self.__connection_string)

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def set_up(self, base):
        base.metadata.create_all(self.get_engine())


class CriptoRepository:
    def insert(self, list_of_criptos):
        with DBConnectionHandler() as db_connection:
            for cripto in list_of_criptos:
                try:
                    new = Cripto(**cripto)
                    db_connection.session.add(new)
                    db_connection.session.commit()
                except:
                    db_connection.session.rollback()
                    raise
                finally:
                    db_connection.session.close()

DBConnectionHandler().set_up(Cripto)
