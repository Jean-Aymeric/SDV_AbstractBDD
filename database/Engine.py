from abc import ABC

from sqlalchemy import URL, create_engine


class Engine(ABC):
    __engine = None

    @classmethod
    def getEngine(cls):
        if cls.__engine is None:
            urlObject = URL.create(
                "mysql",
                username="info",
                password="info",
                host='localhost',
                database="employees")
            cls.__engine = create_engine(urlObject)
        return cls.__engine
