"""Presetner にデータ渡す出力用インターフェース."""

from __future__ import annotations

from dataclasses import dataclass
import typing as tp

from entity.enemyparameter import EnemyParameter


class OutputBoundary(tp.Protocol):
    """Presenter 層にデータ渡す出力用インターフェース."""

    def output(self, data: OutputData) -> None:
        pass


@dataclass
class OutputData:
    """Presenter に渡すデータ."""

    parameter: EnemyParameter
