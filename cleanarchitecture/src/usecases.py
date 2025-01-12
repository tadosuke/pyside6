"""ユースケース層のモジュール."""

from __future__ import annotations

from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


class InputBoundary(metaclass=ABCMeta):

    @abstractmethod
    def input(self):
        pass


class OutputBoundary(metaclass=ABCMeta):

    @abstractmethod
    def output(self):
        pass


class DataAccessInterface(metaclass=ABCMeta):

    @abstractmethod
    def save(self) -> None:
        pass

    @abstractmethod
    def load(self) -> None:
        pass


@dataclass
class InputData:
    pass


@dataclass
class OutputData:
    pass


class UseCaseInteractor(InputBoundary):
    """アプリケーションのルールに基づき、entity 層を操作するクラス.

    :param output: Presenter に渡す出力
    :param data_access: データアクセス先
    """

    def __init__(
            self,
            output: OutputBoundary,
            data_access: DataAccessInterface) -> None:
        self._output = output
        self._data_access = data_access

    def input(self) -> None:
        """(override)コントローラからの入力を受け取る."""
        pass
