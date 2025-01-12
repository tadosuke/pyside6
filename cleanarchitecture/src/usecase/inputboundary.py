"""Controller 層から入力を受け取るインターフェース."""

from __future__ import annotations

from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


class InputBoundary(metaclass=ABCMeta):
    """Controller 層から入力を受け取るインターフェース."""

    @abstractmethod
    def input(self, data: InputData) -> None:
        pass


@dataclass
class InputData:

    id: int = 0
