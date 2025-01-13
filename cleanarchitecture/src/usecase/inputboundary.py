"""Controller 層から入力を受け取るインターフェース."""

from __future__ import annotations

from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


class InputBoundary(metaclass=ABCMeta):
    """Controller 層から入力を受け取るインターフェース."""

    @abstractmethod
    def input(self, data: InputData) -> None:
        """Controller からの入力.

        :param data: 入力データ
        """
        ...


@dataclass
class InputData:
    """Controller からの入力データ."""

    id: int = 0
