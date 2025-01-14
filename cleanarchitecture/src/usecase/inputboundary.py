"""Controller 層から入力を受け取るインターフェース."""

from __future__ import annotations

from abc import ABCMeta, abstractmethod


class InputBoundary(metaclass=ABCMeta):
    """Controller 層から入力を受け取るインターフェース."""

    @abstractmethod
    def set_name(self, name: str) -> None:
        ...

    @abstractmethod
    def set_hp(self, hp: int) -> None:
        ...

    @abstractmethod
    def save(self) -> None:
        ...

    @abstractmethod
    def load(self) -> None:
        ...
