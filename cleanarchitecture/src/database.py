"""データベースモジュール."""


from usecases import DataAccessInterface


class DataAccess(DataAccessInterface):

    def save(self) -> None:
        """(override)"""
        pass

    def load(self) -> None:
        """(override)"""
        pass


class Database:
    pass
