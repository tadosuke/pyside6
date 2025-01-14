"""ファイルアクセス機能を提供するモジュール."""

from __future__ import annotations

import json

from entity.enemyparameter import EnemyParameter
from usecase.dataaccess import DataAccessInterface


#: 保存するファイル名
FILE_NAME = 'enemy_param.json'


class FileAccess(DataAccessInterface):
    """ファイルアクセス機能を提供するクラス."""

    def __init__(self) -> None:
        pass

    def save(self, parameter: EnemyParameter) -> None:
        """(override)エネミーのパラメータを保存する.

        :param parameter: 保存するパラメータ
        """
        data = {
            "name": parameter.name,
            "hp": parameter.hp,
        }
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load(self) -> EnemyParameter:
        """(override)エネミーのパラメータを読み込む.

        :return: 読み込んだパラメータ
        """
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)
            parameter = EnemyParameter()
            parameter.name = data.get("name", "")
            parameter.hp = data.get("hp", 0)
            return parameter
        except Exception:
            return EnemyParameter()
